"""scrapli_community.scrapli.networkdriver.ansync_driver"""

from typing import Any

from scrapli.driver import AsyncNetworkDriver


async def default_async_on_open(conn: AsyncNetworkDriver) -> None:
    """
    Async scrapli_example default on_open callable

    Args:
        conn: AsyncNetworkDriver object

    Returns:
        N/A

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
        conn: AsyncNetworkDriver object

    Returns:
        N/A

    Raises:
        N/A
    """
    # write exit directly to the transport as channel would fail to find the prompt after sending
    # the exit command!
    await conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)
    conn.channel.write(channel_input="exit")
    conn.channel.send_return()


class AsyncScrapliNetworkDriverWithMethods(AsyncNetworkDriver):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Example scrapli community platform class

        Args:
            args: positional args
            kwargs: keyword args

        Returns:
            N/A

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
            N/A

        Raises:
            N/A

        """
        self.channel.send_return()
        result = await self.channel.read()
        print(result)
