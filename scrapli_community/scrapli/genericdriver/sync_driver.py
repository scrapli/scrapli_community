"""scrapli_community.scrapli.genericdriver.sync_driver"""

import time

from scrapli.driver import GenericDriver


def default_sync_on_open(conn: GenericDriver) -> None:
    """
    scrapli_genericdriver default on_open callable

    This is tested with a cisco wlc using auth_bypass so we have to send creds during on open

    Args:
        conn: GenericDriver object

    Returns:
        N/A

    Raises:
        N/A
    """
    time.sleep(0.25)
    conn.channel.write(channel_input=conn.transport.auth_username)
    conn.channel.send_return()
    time.sleep(0.25)
    conn.channel.write(channel_input=conn.transport.auth_password)
    conn.channel.send_return()


def default_sync_on_close(conn: GenericDriver) -> None:
    """
    scrapli_genericdriver default on_close callable

    Args:
        conn: GenericDriver object

    Returns:
        N/A

    Raises:
        N/A

    """
    conn.channel.write(channel_input="logout")
    conn.channel.send_return()
