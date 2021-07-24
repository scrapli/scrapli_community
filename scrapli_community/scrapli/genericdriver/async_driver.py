"""scrapli_community.scrapli.genericdriver._ansync"""
import asyncio

from scrapli.driver import AsyncNetworkDriver


async def default_async_on_open(conn: AsyncNetworkDriver) -> None:
    """
    Async scrapli_genericdriver default on_open callable

    This is tested with a cisco wlc using auth_bypass so we have to send creds during on open

    Args:
        conn: NetworkDriver object

    Returns:
        N/A  # noqa: DAR202

    Raises:
        N/A
    """
    await asyncio.sleep(0.25)
    conn.channel.write(channel_input=conn.transport.auth_username)
    conn.channel.send_return()
    await asyncio.sleep(0.25)
    conn.channel.write(channel_input=conn.transport.auth_password)
    conn.channel.send_return()


async def default_async_on_close(conn: AsyncNetworkDriver) -> None:
    """
    Async scrapli_genericdriver default on_close callable

    Args:
        conn: NetworkDriver object

    Returns:
        N/A  # noqa: DAR202

    Raises:
        N/A

    """
    conn.channel.write(channel_input="logout")
    conn.channel.send_return()
