"""scrapli_community.huawei.vrp.async_driver"""

from typing import Any

from scrapli.driver import AsyncNetworkDriver


async def default_async_on_open(conn: AsyncNetworkDriver) -> None:
    """
    Async huawei_vrp default on_open callable

    Args:
        conn: AsyncNetworkDriver object

    Returns:
        N/A

    Raises:
        N/A

    """
    await conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)
    await conn.send_command(command="screen-length 0 temporary")

    # Attempt to set screen width as a fallback in case the device does not accept the
    # ptyprocess/cols property when using system transport (observed on some firmware versions).
    #
    # On some devices, the command below might not exist (some switches running < V200R019);
    # on others it asks for confirmation (Y/N), and other devices accept the command as-is.
    #
    # Use write() instead of send_command() or send_interactive() to fail silently should the
    # command not exist.
    conn.channel.write(channel_input="screen-width 256\ny\n\n")

    # Make sure that we have a prompt again, and are not stuck in some confirmation loop.
    await conn.channel.get_prompt()


async def default_async_on_close(conn: AsyncNetworkDriver) -> None:
    """
    Async huawei_vrp default on_close callable

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


class AsyncHuaweiVRPDriver(AsyncNetworkDriver):
    def __init__(self, **kwargs: Any) -> None:
        """
        Huawei VRP platform class

        Args:
            kwargs: keyword args

        Returns:
            N/A

        Raises:
            N/A

        """
        # *if* using anything but system transport pop out ptyprocess transport options, leaving
        # anything else
        transport_plugin = kwargs.get("transport", "system")
        if transport_plugin != "system":
            kwargs.get("transport_options", {}).pop("ptyprocess", None)

        super().__init__(**kwargs)
