"""scrapli_community.aethra.atosnt.sync"""
from scrapli.driver import GenericDriver


def default_sync_on_close(conn: GenericDriver) -> None:
    """
    aethra_atosnt default on_close callable

    Args:
        conn: NetworkDriver object

    Returns:
        N/A  # noqa: DAR202

    Raises:
        N/A
    """
    # write exit directly to the transport as channel would fail to find the prompt after sending
    # the exit command!
    conn.transport.write(channel_input="\x04")
    conn.transport.write(channel_input=conn.channel.comms_return_char)
