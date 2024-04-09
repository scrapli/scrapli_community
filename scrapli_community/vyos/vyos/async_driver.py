"""scrapli_community.vyos.vyos.async_driver"""

from scrapli.driver import AsyncNetworkDriver


async def default_async_on_open(conn: AsyncNetworkDriver) -> None:
    """
    Async vyos default on_open callable

    Args:
        conn: AsyncNetworkDriver object

    Returns:
        N/A

    Raises:
        N/A

    """
    await conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)

    await conn.send_command(command="stty cols 100000")


async def default_async_on_close(conn: AsyncNetworkDriver) -> None:
    """
    Async vyos default on_close callable

    Args:
        conn: AsyncNetworkDriver object

    Returns:
        N/A

    Raises:
        N/A

    """
    await conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)

    conn.channel.write(channel_input="exit")
    conn.channel.send_return()
