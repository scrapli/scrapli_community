"""scrapli_community.siemens.roxii.sync"""
from scrapli.driver import NetworkDriver


def default_sync_on_open(conn: NetworkDriver) -> None:
    """
    siemens_roxii on_open callable

    Args:
        conn: NetworkDriver object

    Returns:
        N/A  # noqa: DAR202

    Raises:
        N/A
    """

    conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)


def default_sync_on_close(conn: NetworkDriver) -> None:
    """
    siemens_roxii default on_close callable

    Args:
        conn: NetworkDriver object

    Returns:
        N/A  # noqa: DAR202

    Raises:
        N/A

    """
    conn.channel.write(channel_input="q")
    conn.channel.send_return()
