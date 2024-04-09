"""scrapli_community.alcatel.aos.async_driver"""

from scrapli.driver import AsyncGenericDriver


async def default_async_on_close(conn: AsyncGenericDriver) -> None:
    """
    Async alcatel_aos default on_close callable

    Args:
        conn: AsyncGenericDriver object

    Returns:
        N/A

    Raises:
        N/A

    """
    conn.channel.write(channel_input="exit")
    conn.channel.send_return()
