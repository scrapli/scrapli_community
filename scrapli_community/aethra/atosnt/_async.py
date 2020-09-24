"""scrapli_community.aethra.atosnt._async"""
from scrapli.driver import AsyncGenericDriver


async def default_async_on_close(conn: AsyncGenericDriver) -> None:
    """
    Async aethra_atosnt default on_close callable

    Args:
        conn: NetworkDriver object

    Returns:
        N/A  # noqa: DAR202

    Raises:
        N/A
    """
    # write exit directly to the transport as channel would fail to find the prompt after sending
    # the exit command!
    await conn.transport.write(channel_input="\x04")
    await conn.transport.write(channel_input=conn.channel.comms_return_char)
