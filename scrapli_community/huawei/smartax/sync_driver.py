"""scrapli_community.huawei.smartax.sync_driver"""

from typing import Any

from scrapli.driver import NetworkDriver


def default_sync_on_open(conn: NetworkDriver) -> None:
    """
    huawei_smartax on_open callable

    Args:
        conn: NetworkDriver object

    Returns:
        N/A

    Raises:
        N/A
    """
    conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)
    conn.send_command(command="undo smart")
    conn.send_command(command="scroll")


def default_sync_on_close(conn: NetworkDriver) -> None:
    """
    huawei_smartax default on_close callable

    Args:
        conn: NetworkDriver object

    Returns:
        N/A

    Raises:
        N/A

    """
    conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)
    conn.channel.write(channel_input="quit")
    conn.channel.send_return()
    conn.channel.write(channel_input="y")
    conn.channel.send_return()


class HuaweiSmartAXDriver(NetworkDriver):
    def __init__(self, **kwargs: Any) -> None:
        """
        Huawei SmartAX platform class

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
