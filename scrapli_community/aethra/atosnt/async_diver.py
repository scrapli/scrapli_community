"""scrapli_community.aethra.atosnt.async_driver"""

from scrapli.driver import AsyncGenericDriver


async def default_async_on_close(conn: AsyncGenericDriver) -> None:
    """
    Async aethra_atosnt default on_close callable

    Args:
        conn: AsyncGenericDriver object

    Returns:
        N/A

    Raises:
        N/A

    """
    conn.channel.write(channel_input="\x04")
    conn.channel.send_return()
