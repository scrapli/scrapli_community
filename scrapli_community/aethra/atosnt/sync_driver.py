"""scrapli_community.aethra.atosnt.sync_driver"""

from scrapli.driver import GenericDriver


def default_sync_on_close(conn: GenericDriver) -> None:
    """
    aethra_atosnt default on_close callable

    Args:
        conn: GenericDriver object

    Returns:
        N/A

    Raises:
        N/A

    """
    conn.channel.write(channel_input="\x04")
    conn.channel.send_return()
