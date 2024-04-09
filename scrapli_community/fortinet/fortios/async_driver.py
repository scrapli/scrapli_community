"""scrapli_community.fortinet.fortios.async_driver"""

import asyncio
import re
import textwrap
from typing import Any, List, Optional, Union

from scrapli.driver import AsyncGenericDriver
from scrapli.exceptions import ScrapliCommandFailure, ScrapliTimeout
from scrapli.response import MultiResponse


class AsyncFortinetFortiOSDriver(AsyncGenericDriver):
    """Fortinet FortiOS platform class

    Attributes:
        _vdoms_enabled (bool): True when device is in multi-VDOM mode
        _vdom_list (List[str]): list of VDOMs read from device when needed
        _original_console (str): more|standard, read from device in order to restore it by cleanup
    """

    def __init__(self, **kwargs: Any):
        self._vdoms_enabled: bool = False
        self._vdom_list: List[str] = []
        self._original_console: str = ""
        super().__init__(**kwargs)

    async def _vdoms_status(self) -> bool:
        """Determine whether virtual domains are enabled or not

        Returns:
            True is device is configured with multi VDOM mode
        """
        output = await self.send_command('get system status | grep "Virtual domain configuration"')

        return bool(re.search(r"Virtual domain configuration: (multiple|enable)", output.result))

    async def prepare_session(self) -> None:
        """Prepare session"""

        # check if user configured post-login banner which requires acceptance
        # config system global
        #     set post-login-banner enable
        # end
        initial = await self.channel.read()
        if "(Press 'a' to accept):" in str(initial):
            self.channel.write("a")
        await self.get_prompt()
        self._vdoms_enabled = await self._vdoms_status()
        if self._vdoms_enabled:
            await self.context("global")
        response = await self.send_command("get system console | grep ^output")
        self._original_console = re.findall(r".*: (\w+)", response.result)[0]
        if self._original_console != "standard":
            disable_paging = textwrap.dedent(
                """\
                config system console
                set output standard
                end"""
            )
            if self._vdoms_enabled:  # we exit from global too
                disable_paging += "\nend"
            await self.send_commands(disable_paging.splitlines())
        elif self._vdoms_enabled:
            await self.context("system")

    async def cleanup_session(self) -> None:
        """Restore paging if necessary"""
        if self._original_console != "standard":
            if self._vdoms_enabled:
                await self.context("global")
            else:
                await self._to_system()
            restore_console = textwrap.dedent(
                f"""\
                config system console
                set output {self._original_console}
                end"""
            )
            await self.send_commands(restore_console.splitlines())

    async def _to_system(self) -> None:
        """Abort everything and go to the root prompt

        Note:
            This can't handle all cases, user needs to ensure all command blocks are closed.
            This won't exit deeply nested config blocks!
        """
        prompt = await self.get_prompt()
        if "(" in prompt:
            await self.send_commands(["abort", "end"])

    async def gather_vdoms(self) -> Union[None, List[str]]:
        """Gather list of VDOMs

        Returns:
            None: if device is not in multi VDOM mode
            List[str]: list of VDOM names configured
        """

        if not self._vdoms_enabled:
            # device is not in multi VDOM mode
            return None
        await self._to_system()
        output = await self.send_command('show | grep "config vdom" -f -A1')
        # """
        # FIREWALL # show | grep "config vdom" -f -A1
        # config vdom
        # edit root
        # --
        # config vdom
        # edit root
        # --
        # config vdom
        # edit test1
        # """
        self._vdom_list = list(set(re.findall(r"^edit (\w+)$", output.result, re.M)))
        return self._vdom_list

    async def context(self, context: str) -> Union[None, str]:
        """Change context / VDOM

        This method will abort any config block / VDOM and change to the specified context.
        If device is not in multi-VDOM mode, do nothing. If specified VDOM is not pre-defined,
        query device for available VDOMs to check if it's possible.

        Pre-defined contexts:
            * system : root prompt, not in any config block or VDOM
            * global : in global context
            * root : default VDOM which cannot be renamed

        Args:
            context (str): VDOM name or pre-defined context name

        Returns:
            None if context change is not possible or context name

        Raises:
            ScrapliCommandFailure: on context changing errors

        """
        self.logger.debug("Changing to context %s", context)
        if not self._vdoms_enabled:
            return None
        # if context is a non-predefined one, gather VDOM list from device
        if not self._vdom_list and context not in ["system", "global", "root"]:
            # gather list of VDOMs
            await self.gather_vdoms()  # slow :(
        else:
            await self._to_system()
        if context == "system":
            # we are already here
            pass
        elif context == "global":
            response = await self.send_command("config global")
            if response.failed:
                raise ScrapliCommandFailure(f"Couldn't change to {context} context!")
        elif context in self._vdom_list or context == "root":
            responses = await self.send_commands(["config vdom", f"edit {context}"])
            if responses[-1].failed:
                raise ScrapliCommandFailure(f"Couldn't change to {context} context!")
        else:
            raise ScrapliCommandFailure(f"Tried to change to {context}, but it doesn't exists!")

        return context

    async def send_config(self, config: str, **kwargs: Any) -> None:
        """Not implemented on FortiOS

        Args:
            config (str): config text
            kwargs: other arguments

        Raises:
            NotImplementedError: this function is not implemented
        """
        raise NotImplementedError("send_config not implemented for FortiOS")

    async def send_configs(self, configs: List[str], **kwargs: Any) -> None:
        """Not implemented on FortiOS

        Args:
            configs (List[str]): config text
            kwargs: other arguments

        Raises:
            NotImplementedError: this function is not implemented
        """
        raise NotImplementedError("send_config not implemented for FortiOS")

    # pylama:ignore=C901
    async def send_commands(
        self,
        commands: List[str],
        *,
        batch_mode: bool = False,
        strip_prompt: bool = True,
        failed_when_contains: Optional[Union[str, List[str]]] = None,
        stop_on_failed: bool = False,
        eager: bool = False,
        eager_input: bool = False,
        timeout_ops: Optional[float] = None,
    ) -> MultiResponse:
        """Send multiple commands to device

        This method adds capability to use FortiOS batch mode which applies commands after all
        commands are sent. This is useful for configuration where we want to apply more things
        at once to avoid losing mgmt connectivity. E.g. when changing mgmt IP and default gw.

        If device is in multi-VDOM mode, please make sure you select full scope of your commands.

        Example of multi-VDOM batch commands::
            config vdom
                edit test1
                    config system interface
                        edit mgmt
                            set ip 1.1.1.1/30
                        next
                    end
                end
            end

        Example device output with batch result::

            Code: sent command

            0: config system global
            -61: unset set post-login-banner enable
            -61: unset post-login-banner enable
            0: unset post-login-banner
            0: end

            Code is error code. 0 means ok. The above example shows that mistyped commands gave
            error with code -61.

        Args:
            commands: list of strings to send to device in config mode
            batch_mode: True/False to indicate we want batch mode processing
            strip_prompt: True/False strip prompt from returned output
            failed_when_contains: string or list of strings indicating failure if found in response
            stop_on_failed: True/False stop executing commands if a command fails, returns results
                as of current execution
            eager: if eager is True we do not read until prompt is seen at each command sent to the
                channel. Do *not* use this unless you know what you are doing as it is possible that
                it can make scrapli less reliable!
            eager_input: when true does *not* try to read our input off the channel -- generally
                this should be left alone unless you know what you are doing!
            timeout_ops: timeout ops value for this operation; only sets the timeout_ops value for
                the duration of the operation, value is reset to initial value after operation is
                completed. Note that this is the timeout value PER CONFIG sent, not for the total
                of the configs being sent!

        Returns:
            MultiResponse: Scrapli MultiResponse object

        Raises:
            ScrapliCommandFailure: on errors entering/exiting batch mode
            ScrapliTimeout: on batch execution timeout
        """
        # sanity check, we need more than 1 valid lines to make batch_mode sane
        if batch_mode and len([config for config in commands if config.strip()]) < 2:
            batch_mode = False

        if batch_mode:
            # enable batch run
            if self._vdoms_enabled:
                await self.context("global")
            response = await self.send_command(
                "execute batch start", failed_when_contains="Unknown", timeout_ops=5
            )
            if response.failed:
                raise ScrapliCommandFailure(
                    "Couldn't enter batch mode, check context! (only single mode or "
                    "global VDOM supports batch mode)"
                )

        responses = await super().send_commands(
            commands,
            strip_prompt=strip_prompt,
            failed_when_contains=failed_when_contains,
            stop_on_failed=stop_on_failed,
            eager=eager,
            eager_input=eager_input,
            timeout_ops=timeout_ops,
        )

        if batch_mode:
            # stop batch run
            response = await self.send_command(
                "execute batch end", failed_when_contains="Unknown", timeout_ops=5
            )
            if response.failed:
                raise ScrapliCommandFailure("Couldn't stop batch mode")
            # check batch status
            check_no = 0
            wait = 1.0
            while check_no * wait < (timeout_ops or 30):
                response = await self.send_command(
                    "execute batch status", failed_when_contains="Unknown"
                )
                if "batch mode is stopped" in response.result:
                    break
                check_no += 1
                await asyncio.sleep(wait)
            else:
                raise ScrapliTimeout("Batch run timed out")
            # check batch results
            response = await self.send_command(
                "execute batch lastlog", failed_when_contains="Unknown", timeout_ops=5
            )
            if response.failed:
                raise ScrapliCommandFailure("Couldn't list batch results")
            # set config line failed where batch returned non-zero error code
            for i, line in enumerate(response.result.splitlines()):
                code = line.split(sep=": ")[0]
                if code != "0":
                    responses[i].failed = True

        return responses


async def default_async_on_open(conn: AsyncFortinetFortiOSDriver) -> None:
    """
    Async fortinet_fortios default on_open callable

    Args:
        conn: AsyncNetworkDriver object

    Returns:
        N/A

    Raises:
        N/A
    """
    await conn.prepare_session()


async def default_async_on_close(conn: AsyncFortinetFortiOSDriver) -> None:
    """
    Async fortinet_wlc default on_close callable

    Args:
        conn: AsyncNetworkDriver object

    Returns:
        N/A

    Raises:
        N/A
    """
    await conn.cleanup_session()
    conn.channel.write(channel_input="exit")
    conn.channel.send_return()
