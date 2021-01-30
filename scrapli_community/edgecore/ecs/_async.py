"""scrapli_community.edgecore.ecs._async"""
from scrapli.driver import AsyncNetworkDriver


async def default_async_on_open(conn: AsyncNetworkDriver) -> None:
    """
    Async edgecore_ecs default on_open callable

    Args:
        conn: NetworkDriver object

    Returns:
        N/A  # noqa: DAR202

    Raises:
        N/A

    """
    await conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)

    await conn.send_command(command="terminal length 0")
    await conn.send_command(command="terminal width 300")


async def default_async_on_close(conn: AsyncNetworkDriver) -> None:
    """
    Async edgecore_ecs default on_close callable

    Args:
        conn: NetworkDriver object

    Returns:
        N/A  # noqa: DAR202

    Raises:
        N/A

    """
    await conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)

    await conn.channel.write(channel_input="exit")
    conn.channel.send_return()
