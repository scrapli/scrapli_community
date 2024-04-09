"""scrapli_community.mikrotik.routeros.async_driver"""

from typing import Any, List, Optional, Union

from scrapli.driver import AsyncGenericDriver
from scrapli.response import Response


async def default_async_on_close(conn: AsyncGenericDriver) -> None:
    """
    Async mikrotik_routeros default on_close callable

    Args:
        conn: AsyncGenericDriver object

    Returns:
        N/A

    Raises:
        N/A

    """
    conn.channel.write(channel_input="/quit")
    conn.channel.send_return()


class AsyncMikrotikRouterOSDriver(AsyncGenericDriver):
    def __init__(self, **kwargs: Any) -> None:
        """
        Mikrotik RouterOS platform class

        Args:
            kwargs: keyword args

        Returns:
            N/A

        Raises:
            N/A

        """

        # Append login options to the username according to
        # https://wiki.mikrotik.com/wiki/Manual:Console_login_process
        kwargs["auth_username"] += "+cet511w4098h"

        super().__init__(**kwargs)

    async def send_command(
        self,
        command: str,
        *,
        strip_prompt: bool = True,
        failed_when_contains: Optional[Union[str, List[str]]] = None,
        eager_input: bool = False,
        timeout_ops: Optional[float] = None,
    ) -> Response:
        """
        mikrotik_routeros send_command method

        Args:
            command: string to send to device in privilege exec mode
            strip_prompt: True/False strip prompt from returned output
            failed_when_contains: string or list of strings indicating failure if found in response
            eager_input: when true does *not* try to read our input off the channel -- generally
                this should be left alone unless you know what you are doing!
            timeout_ops: timeout ops value for this operation; only sets the timeout_ops value for
                the duration of the operation, value is reset to initial value after operation is
                completed

        Returns:
            Response: Scrapli Response object

        Raises:
            N/A

        """

        # RouterOS echoes the prompt/pattern twice after sending a command,
        # modify the prompt pattern accordingly to catch both echoes.
        #
        # [user@HOSTNAME]> /command\r\n[user@HOSTNAME]> /command\r\nOUTPUT...
        #
        old_comms_prompt_pattern = self.comms_prompt_pattern
        self.comms_prompt_pattern = f"{old_comms_prompt_pattern}.*{old_comms_prompt_pattern}"

        response = await super().send_command(
            command,
            strip_prompt=strip_prompt,
            failed_when_contains=failed_when_contains,
            eager_input=eager_input,
            timeout_ops=timeout_ops,
        )

        # Change the prompt pattern back to the original one.
        self.comms_prompt_pattern = old_comms_prompt_pattern

        # Since the command is echoed twice, and scrapli only removes it once, we need to
        # manually remove the second command echo by stripping the first line from the output.
        if response.result.count("\n") > 0 and command in response.result.split("\n")[0]:
            response.result = "\n".join(response.result.split("\n")[1:])

        return response
