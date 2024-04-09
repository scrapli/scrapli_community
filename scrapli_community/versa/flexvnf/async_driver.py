"""scrapli_community.versa.flexvnf.ansync_driver"""

from scrapli.driver import AsyncNetworkDriver


async def default_async_on_open(conn: AsyncNetworkDriver) -> None:
    """
    Async versa_flexvnf default on_open callable

    Args:
        conn: AsyncNetworkDriver object

    Returns:
        N/A

    Raises:
        N/A
    """
    await conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)
    await conn.send_command(command="set complete-on-space false")
    await conn.send_command(command="set paginate false")
    await conn.send_command(command="set screen width 512")


async def default_async_on_close(conn: AsyncNetworkDriver) -> None:
    """
    Async versa_flexvnf default on_close callable

    Args:
        conn: AsyncNetworkDriver object

    Returns:
        N/A

    Raises:
        N/A
    """
    # write exit directly to the transport as channel would fail to find the prompt after sending
    # the exit command!
    await conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)
    conn.channel.write(channel_input="exit")
    conn.channel.write(channel_input="logout")
