"""scrapli_community.ruckus.unleashed.sync_driver"""

from scrapli.driver import NetworkDriver


def default_sync_on_open(conn: NetworkDriver) -> None:
    """
    ruckus_unleashed default on_open callable

    Args:
        conn: NetworkDriver object

    Returns:
        N/A

    Raises:
        N/A
    """
    # Since Ruckus Unleashed devices do not use true SSH authentication, after the initial
    # connection is established, authentication is handled using Scrapli's built-in telnet
    # authentication:
    # https://github.com/carlmontanari/scrapli/blob/main/scrapli/channel/sync_channel.py#L327
    # Auth Bypass Reference:
    # https://carlmontanari.github.io/scrapli/user_guide/advanced_usage/#auth-bypass
    conn.channel.channel_authenticate_telnet(
        auth_username=conn.auth_username, auth_password=conn.auth_password
    )
    conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)


def default_sync_on_close(conn: NetworkDriver) -> None:
    """
    ruckus_unleashed default on_close callable

    Args:
        conn: NetworkDriver object

    Returns:
        N/A

    Raises:
        N/A
    """
    conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)
    conn.channel.write(channel_input="exit")
    conn.channel.send_return()
