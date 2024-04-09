"""scrapli_community.cisco.aireos.async_driver"""

import time

from scrapli.driver import AsyncNetworkDriver


async def default_async_on_open(conn: AsyncNetworkDriver) -> None:
    """
    Async cisco_aireos default on_open callable

    Args:
        conn: NetworkDriver object

    Returns:
        N/A

    Raises:
        N/A

    """
    # Due to Cisco AireOS devices not having a true SSH authentication, the following
    # technique has been employed to send the auth_username and auth_password to the device
    # to handle the initial authentication.
    # Reference Doco:
    # https://carlmontanari.github.io/scrapli/user_guide/advanced_usage/#auth-bypass
    # https://github.com/carlmontanari/scrapli/blob/master/examples/non_core_device/wlc.py#L25
    time.sleep(0.25)
    conn.channel.write(conn.auth_username)
    conn.channel.send_return()
    time.sleep(0.25)
    conn.channel.write(conn.auth_password)
    conn.channel.send_return()
    await conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)
    await conn.send_command(command="config paging disable")


async def default_async_on_close(conn: AsyncNetworkDriver) -> None:
    """
    Async cisco_aireos default on_close callable

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
