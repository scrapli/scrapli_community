"""scrapli_community.fortinet.wlc.async_driver"""

from scrapli.driver import AsyncNetworkDriver


async def default_async_on_open(conn: AsyncNetworkDriver) -> None:
    """
    Async fortinet_wlc default on_open callable

    Args:
        conn: AsyncNetworkDriver object

    Returns:
        N/A

    Raises:
        N/A
    """

    await conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)


async def default_async_on_close(conn: AsyncNetworkDriver) -> None:
    """
    Async fortinet_wlc default on_close callable

    Args:
        conn: AsyncNetworkDriver object

    Returns:
        N/A

    Raises:
        N/A
    """
    conn.channel.write(channel_input="q")
    conn.channel.send_return()
