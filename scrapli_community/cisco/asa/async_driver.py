"""scrapli_community.cisco.asa.async_driver"""

from scrapli.driver import AsyncNetworkDriver


async def default_async_on_open(conn: AsyncNetworkDriver) -> None:
    """
    Async cisco_asa default on_open callable

    Args:
        conn: NetworkDriver object

    Returns:
        N/A

    Raises:
        N/A

    """
    await conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)
    await conn.send_command(command="terminal pager 0")
    await conn.send_config(config="terminal width 511")


async def read_only_async_on_open(conn: AsyncNetworkDriver) -> None:
    """
    Async cisco_asa read-only on_open callable

    Args:
        conn: NetworkDriver object

    Returns:
        N/A

    Raises:
        N/A

    """
    await conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)
    await conn.send_command(command="terminal pager 0")


async def default_async_on_close(conn: AsyncNetworkDriver) -> None:
    """
    Async cisco_asa default on_close callable

    Args:
        conn: NetworkDriver object

    Returns:
        N/A

    Raises:
        N/A

    """
    await conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)
    conn.channel.write(channel_input="logout")
    conn.channel.send_return()
