"""scrapli_community.cumulus.linux.async_driver"""

from scrapli.driver import AsyncNetworkDriver


async def default_async_on_open(conn: AsyncNetworkDriver) -> None:
    """
    cumulus_linux on_open callable

    Args:
        conn: AsyncNetworkDriver object

    Returns:
        None

    Raises:
        N/A
    """
    await conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)


async def default_async_on_close(conn: AsyncNetworkDriver) -> None:
    """
    cumulus_linux default on_close callable

    Args:
        conn: AsyncNetworkDriver object

    Returns:
        None

    Raises:
        N/A

    """
    await conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)
    conn.channel.write(channel_input="exit")
    conn.channel.send_return()
