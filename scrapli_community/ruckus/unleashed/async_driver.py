"""scrapli_community.ruckus.unleashed.async_driver"""

from scrapli.driver import AsyncNetworkDriver


async def default_async_on_open(conn: AsyncNetworkDriver) -> None:
    """
    Async ruckus_unleashed default on_open callable

    Args:
        conn: AsyncNetworkDriver object

    Returns:
        N/A

    Raises:
        N/A
    """
    # Since Ruckus Unleashed devices do not use true SSH authentication, after the initial
    # connection is established, authentication is handled using Scrapli's built-in telnet
    # authentication:
    # https://github.com/carlmontanari/scrapli/blob/main/scrapli/channel/async_channel.py#L331
    # Auth Bypass Reference:
    # https://carlmontanari.github.io/scrapli/user_guide/advanced_usage/#auth-bypass
    await conn.channel.channel_authenticate_telnet(
        auth_username=conn.auth_username, auth_password=conn.auth_password
    )
    await conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)


async def default_async_on_close(conn: AsyncNetworkDriver) -> None:
    """
    Async ruckus_unleashed default on_close callable

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
