"""scrapli_community.mikrotik.routeros._async"""
from typing import Any, List, Optional, Union

from scrapli.driver import AsyncGenericDriver
from scrapli.response import Response


async def default_async_on_close(conn: AsyncGenericDriver) -> None:
    """
    Async mikrotik_routeros default on_close callable

    Args:
        conn: NetworkDriver object

    Returns:
        N/A  # noqa: DAR202

    Raises:
        N/A
    """
    # write exit directly to the transport as channel would fail to find the prompt after sending
    # the exit command!
    conn.transport.write(channel_input="/quit")
    conn.transport.write(channel_input=conn.channel.comms_return_char)


class AsyncMikrotikRouterOSDriver(AsyncGenericDriver):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Mikrotik RouterOS platform class

        Args:
            args: positional args
            kwargs: keyword args

        Returns:
            N/A  # noqa: DAR202

        Raises:
            N/A

        """

        # Append login options to the username according to
        # https://wiki.mikrotik.com/wiki/Manual:Console_login_process
        kwargs["auth_username"] += "+cet511w4098h"

        super().__init__(*args, **kwargs)

    async def send_command(
        self,
        command: str,
        strip_prompt: bool = True,
        failed_when_contains: Optional[Union[str, List[str]]] = None,
        *,
        timeout_ops: Optional[float] = None,
    ) -> Response:
        """
        mikrotik_routeros send_command method

        Args:
            command: string to send to device in privilege exec mode
            strip_prompt: True/False strip prompt from returned output
            failed_when_contains: string or list of strings indicating failure if found in response
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
        old_comms_prompt_pattern = self.channel.comms_prompt_pattern
        self.channel.comms_prompt_pattern = (
            f"{old_comms_prompt_pattern}.*{old_comms_prompt_pattern}"
        )

        response = await super().send_command(
            command, strip_prompt, failed_when_contains, timeout_ops=timeout_ops
        )

        # Change the prompt pattern back to the original one.
        self.channel.comms_prompt_pattern = old_comms_prompt_pattern

        # Since the command is echoed twice, and scrapli only removes it once, we need to
        # manually remove the second command echo by stripping the first line from the output.
        if response.result.count("\n") > 0 and command in response.result.split("\n")[0]:
            response.result = "\n".join(response.result.split("\n")[1:])

        return response
