"""scrapli_community.scrapli.genericdriver.sync"""
import time

from scrapli.driver import NetworkDriver


def default_sync_on_open(conn: NetworkDriver) -> None:
    """
    scrapli_genericdriver default on_open callable

    This is tested with a cisco wlc using auth_bypass so we have to send creds during on open

    Args:
        conn: NetworkDriver object

    Returns:
        N/A  # noqa: DAR202

    Raises:
        N/A
    """
    time.sleep(0.25)
    conn.channel.write(channel_input=conn.transport.auth_username)
    conn.channel.send_return()
    time.sleep(0.25)
    conn.channel.write(channel_input=conn.transport.auth_password)
    conn.channel.send_return()


def default_sync_on_close(conn: NetworkDriver) -> None:
    """
    scrapli_genericdriver default on_close callable

    Args:
        conn: NetworkDriver object

    Returns:
        N/A  # noqa: DAR202

    Raises:
        N/A

    """
    conn.channel.write(channel_input="logout")
    conn.channel.send_return()
