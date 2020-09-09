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
    # write exit directly to the transport as channel would fail to find the prompt after sending
    # the exit command!
    await conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)

    await conn.transport.write(channel_input="exit")
    await conn.transport.write(channel_input=conn.channel.comms_return_char)
