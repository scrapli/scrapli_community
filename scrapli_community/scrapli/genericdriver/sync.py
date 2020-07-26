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
    conn.transport.write(channel_input=conn.transport.auth_username)
    conn.transport.write(channel_input=conn.channel.comms_return_char)
    time.sleep(0.25)
    conn.transport.write(channel_input=conn.transport.auth_password)
    conn.transport.write(channel_input=conn.channel.comms_return_char)


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
    # write exit directly to the transport as channel would fail to find the prompt after sending
    # the exit command!
    conn.transport.write(channel_input="logout")
    conn.transport.write(channel_input=conn.channel.comms_return_char)
