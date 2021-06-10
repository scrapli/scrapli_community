"""scrapli_community.alcatel.aos._async"""
from scrapli.driver import AsyncGenericDriver


async def default_async_on_close(conn: AsyncGenericDriver) -> None:
    """
    Async alcatel_aos default on_close callable

    Args:
        conn: NetworkDriver object

    Returns:
        N/A

    Raises:
        N/A

    """
    conn.channel.write(channel_input="exit")
    conn.channel.send_return()
