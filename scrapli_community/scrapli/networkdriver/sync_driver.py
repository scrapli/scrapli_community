"""scrapli_community.scrapli.networkdriver.sync_driver"""

from typing import Any

from scrapli.driver import NetworkDriver


def default_sync_on_open(conn: NetworkDriver) -> None:
    """
    scrapli_example default on_open callable

    Args:
        conn: NetworkDriver object

    Returns:
        N/A

    Raises:
        N/A
    """
    conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)
    conn.send_command(command="terminal length 0")
    conn.send_command(command="terminal width 512")


def default_sync_on_close(conn: NetworkDriver) -> None:
    """
    scrapli_example default on_close callable

    Args:
        conn: NetworkDriver object

    Returns:
        N/A

    Raises:
        N/A
    """
    # write exit directly to the transport as channel would fail to find the prompt after sending
    # the exit command!
    conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)
    conn.channel.write(channel_input="exit")
    conn.channel.send_return()


class ScrapliNetworkDriverWithMethods(NetworkDriver):
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

    def example_method(self) -> None:
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
        print(self.channel.read())
