"""scrapli_community.nokia.sros._async"""
from scrapli.driver import AsyncNetworkDriver


async def default_async_on_open(conn: AsyncNetworkDriver) -> None:
    """
    nokia_sros on_open callable

    Args:
        conn: NetworkDriver object

    Returns:
        None

    Raises:
        N/A
    """
    await conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)
    await conn.send_command(command="environment command-completion space false")
    await conn.send_command(command="environment console width 512")
    await conn.send_command(command="environment more false")
    await conn.send_command(command="//environment no more")


async def default_async_on_close(conn: AsyncNetworkDriver) -> None:
    """
    nokia_sros default on_close callable

    Args:
        conn: NetworkDriver object

    Returns:
        None

    Raises:
        N/A

    """
    await conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)
    conn.channel.write(channel_input="logout")
    conn.channel.send_return()
