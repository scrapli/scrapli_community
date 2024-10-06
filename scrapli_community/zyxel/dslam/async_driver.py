"""scrapli_community.zyxel.dslam.zyxel_dslam"""

from time import sleep
from typing import Any

from scrapli.driver import AsyncNetworkDriver


async def default_async_on_open(conn: AsyncNetworkDriver) -> None:
    """
    Async zyxel_dslam default on_open callable

    Args:
        conn: AsyncNetworkDriver object

    Returns:
        N/A

    Raises:
        N/A
    """
    await conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)


async def default_async_on_close(conn: AsyncNetworkDriver) -> None:
    """
    Async zyxel_dslam default on_close callable

    Args:
        conn: AsyncNetworkDriver object

    Returns:
        N/A

    Raises:
        N/A
    """
    # write exit directly to the transport as channel would fail to find the prompt after sending
    # the exit command!
    # sleep is required to ensure the exit command is processed before the connection is closed
    # otherwise ssh2.exceptions.SocketRecvError is triggered
    await conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)
    conn.channel.write(channel_input="exit")
    conn.channel.send_return()
    sleep(0.1)


class AsyncZyxelDSLAMDriver(AsyncNetworkDriver):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Zyxel DSLAM community platform class

        Args:
            args: positional args
            kwargs: keyword args

        Returns:
            N/A

        Raises:
            N/A

        """
        super().__init__(*args, **kwargs)
