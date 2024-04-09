"""scrapli_community.vyos.vyos.sync_driver"""

from scrapli.driver import NetworkDriver


def default_sync_on_open(conn: NetworkDriver) -> None:
    """
    vyos on_open callable

    Args:
        conn: NetworkDriver object

    Returns:
        N/A

    Raises:
        N/A

    """
    conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)

    conn.send_command(command="stty cols 100000")


def default_sync_on_close(conn: NetworkDriver) -> None:
    """
    vyos default on_close callable

    Args:
        conn: NetworkDriver object

    Returns:
        N/A

    Raises:
        N/A
    """
    conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)

    conn.channel.write(channel_input="exit")
    conn.channel.send_return()
