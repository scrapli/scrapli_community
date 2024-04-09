"""scrapli_community.nokia.nokia_srlinux.sync_driver"""

from scrapli.driver import NetworkDriver


def default_sync_on_open(conn: NetworkDriver) -> None:
    """
    nokia_srlinux on_open callable

    Args:
        conn: NetworkDriver object

    Returns:
        None

    Raises:
        N/A
    """
    conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)
    conn.send_command(command="environment cli-engine type basic")
    conn.send_command(command="environment complete-on-space false")


def default_sync_on_close(conn: NetworkDriver) -> None:
    """
    nokia_srlinux default on_close callable

    Args:
        conn: NetworkDriver object

    Returns:
        None

    Raises:
        N/A

    """
    conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)
    conn.channel.write(channel_input="logout")
    conn.channel.send_return()
