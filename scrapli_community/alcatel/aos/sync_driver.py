"""scrapli_community.alcatel.aos.sync_driver"""

from scrapli.driver import GenericDriver


def default_sync_on_close(conn: GenericDriver) -> None:
    """
    alcatel_aos default on_close callable

    Args:
        conn: GenericDriver object

    Returns:
        N/A

    Raises:
        N/A

    """
    conn.channel.write(channel_input="exit")
    conn.channel.send_return()
