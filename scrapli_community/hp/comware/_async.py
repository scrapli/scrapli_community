"""scrapli_community.hp.comware._async"""
from typing import Any

from scrapli.driver import AsyncNetworkDriver


async def default_async_on_open(conn: AsyncNetworkDriver) -> None:
    """
    Async hp_comware default on_open callable

    Args:
        conn: NetworkDriver object

    Returns:
        N/A  # noqa: DAR202

    Raises:
        N/A

    """
    await conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)
    await conn.send_command(command="screen-length disable")


async def default_async_on_close(conn: AsyncNetworkDriver) -> None:
    """
    Async hp_comware default on_close callable

    Args:
        conn: NetworkDriver object

    Returns:
        N/A  # noqa: DAR202

    Raises:
        N/A

    """
    await conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)
    conn.channel.write(channel_input="quit")
    conn.channel.send_return()


class AsyncHPComwareDriver(AsyncNetworkDriver):
    def __init__(self, **kwargs: Any) -> None:
        """
        HP Comware platform class

        Args:
            kwargs: keyword args

        Returns:
            N/A  # noqa: DAR202

        Raises:
            N/A

        """
        # *if* using anything but system transport pop out ptyprocess transport options, leaving
        # anything else
        transport_plugin = kwargs.get("transport", "system")
        if transport_plugin != "system":
            kwargs.get("transport_options", {}).pop("ptyprocess")

        super().__init__(**kwargs)
