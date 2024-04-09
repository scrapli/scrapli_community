"""scrapli_community.nokia.nokia_srlinux.async_driver"""

from scrapli.driver import AsyncNetworkDriver


async def default_async_on_open(conn: AsyncNetworkDriver) -> None:
    """
    nokia_srlinux on_open callable

    Args:
        conn: AsyncNetworkDriver object

    Returns:
        None

    Raises:
        N/A
    """
    await conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)
    await conn.send_command(command="environment cli-engine type basic")
    await conn.send_command(command="environment complete-on-space false")


async def default_async_on_close(conn: AsyncNetworkDriver) -> None:
    """
    nokia_srlinux default on_close callable

    Args:
        conn: AsyncNetworkDriver object

    Returns:
        None

    Raises:
        N/A

    """
    await conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)
    conn.channel.write(channel_input="logout")
    conn.channel.send_return()
