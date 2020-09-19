"""scrapli_community.scrapli.networkdriver._ansync"""
from typing import Any

from scrapli.driver import AsyncNetworkDriver


async def default_async_on_open(conn: AsyncNetworkDriver) -> None:
    """
    Async scrapli_example default on_open callable

    Args:
        conn: NetworkDriver object

    Returns:
        N/A  # noqa: DAR202

    Raises:
        N/A
    """
    await conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)
    await conn.send_command(command="terminal length 0")
    await conn.send_command(command="terminal width 512")


async def default_async_on_close(conn: AsyncNetworkDriver) -> None:
    """
    Async scrapli_example default on_close callable

    Args:
        conn: NetworkDriver object

    Returns:
        N/A  # noqa: DAR202

    Raises:
        N/A
    """
    # write exit directly to the transport as channel would fail to find the prompt after sending
    # the exit command!
    await conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)
    conn.transport.write(channel_input="exit")
    conn.transport.write(channel_input=conn.channel.comms_return_char)


class AsyncScrapliNetworkDriverWithMethods(AsyncNetworkDriver):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Example scrapli community platform class

        Args:
            args: positional args
            kwargs: keyword args

        Returns:
            N/A  # noqa: DAR202

        Raises:
            N/A

        """
        super().__init__(*args, **kwargs)

    async def example_method(self) -> None:
        """
        Example scrapli community method

        Args:
            N/A

        Returns:
            N/A  # noqa: DAR202

        Raises:
            N/A

        """
        self.transport.write("\n")
        result = await self.transport.read()
        print(result)
