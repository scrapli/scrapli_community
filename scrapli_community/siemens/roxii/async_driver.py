"""scrapli_community.siemens.roxii._async"""
from scrapli.driver import AsyncNetworkDriver


async def default_async_on_open(conn: AsyncNetworkDriver) -> None:
    """
    Async siemens_roxii default on_open callable

    Args:
        conn: NetworkDriver object

    Returns:
        N/A  # noqa: DAR202

    Raises:
        N/A
    """

    await conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)


async def default_async_on_close(conn: AsyncNetworkDriver) -> None:
    """
    Async siemens_roxii default on_close callable

    Args:
        conn: NetworkDriver object

    Returns:
        N/A  # noqa: DAR202

    Raises:
        N/A
    """
    conn.channel.write(channel_input="q")
    conn.channel.send_return()
