"""scrapli_community.zyxel.dslam.zyxel_dslam"""

from time import sleep
from typing import Any

from scrapli.driver import NetworkDriver


def default_sync_on_open(conn: NetworkDriver) -> None:
    """
    zyxel_dslam default on_open callable

    Args:
        conn: NetworkDriver object

    Returns:
        N/A

    Raises:
        N/A
    """
    conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)


def default_sync_on_close(conn: NetworkDriver) -> None:
    """
    zyxel_dslam default on_close callable

    Args:
        conn: NetworkDriver object

    Returns:
        N/A

    Raises:
        N/A
    """
    # write exit directly to the transport as channel would fail to find the prompt after sending
    # the exit command!
    # sleep is required to ensure the exit command is processed before the connection is closed
    # otherwise ssh2.exceptions.SocketRecvError is triggered
    conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)
    conn.channel.write(channel_input="exit")
    conn.channel.send_return()
    sleep(0.1)


class ZyxelDSLAMDriver(NetworkDriver):
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
