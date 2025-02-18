"""scrapli_community.dell.enterprisesonic.async_driver"""

from scrapli.driver import AsyncNetworkDriver


async def default_async_on_open(conn: AsyncNetworkDriver) -> None:
    """
    SONiC on_open callable

    Args:
        conn: AsyncNetworkDriver object

    Returns:
        None

    Raises:
        N/A
    """
    await conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)
    await conn.send_command(command="terminal length 0")


async def default_async_on_close(conn: AsyncNetworkDriver) -> None:
    """
    SONiC default on_close callable

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
