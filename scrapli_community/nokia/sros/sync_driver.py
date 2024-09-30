"""scrapli_community.nokia.sros.sync_driver"""

from scrapli.driver import NetworkDriver


def default_sync_on_open(conn: NetworkDriver) -> None:
    """
    nokia_sros on_open callable

    Args:
        conn: NetworkDriver object

    Returns:
        None

    Raises:
        N/A
    """
    conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)
    conn.send_command(command="environment command-completion space false")
    conn.send_command(command="environment console width 512")
    conn.send_command(command="environment more false")
    conn.send_command(command="//environment no more")


def classic_default_sync_on_open(conn: NetworkDriver) -> None:
    """
    nokia_sros classic mode on_open callable

    Args:
        conn: NetworkDriver object

    Returns:
        None

    Raises:
        N/A
    """
    conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)
    conn.send_command(command="environment no more")


def classic_aram_sync_on_open(conn: NetworkDriver) -> None:
    """
    nokia_sros aram mode on_open callable

    Args:
        conn: NetworkDriver object

    Returns:
        None

    Raises:
        N/A
    """
    conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)
    conn.send_command(command="environment mode batch")
    conn.send_command(command="environment inhibit-alarms")
    conn.send_command(command="environment print no-more")
    conn.send_command(command="exit all")


def default_sync_on_close(conn: NetworkDriver) -> None:
    """
    nokia_sros default on_close callable

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
