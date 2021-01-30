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
    conn.channel.write(channel_input="\x04")
    conn.channel.send_return()
