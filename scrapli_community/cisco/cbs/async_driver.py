"""scrapli_community.cisco.cbs.async_driver"""

from scrapli.driver import AsyncNetworkDriver


async def default_async_on_open(conn: AsyncNetworkDriver) -> None:
    """
    cisco_cbs on_open callable

    Args:
        conn: AsyncNetworkDriver object

    Returns:
        None

    Raises:
        N/A

    """
    await conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)
    await conn.send_command(command="terminal datadump")
    await conn.send_command(command="terminal width 0")


async def default_async_on_close(conn: AsyncNetworkDriver) -> None:
    """
    cisco_cbs default on_close callable

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
