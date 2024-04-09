"""scrapli_community.vyos.vyos.vyos"""

from scrapli.driver.network.base_driver import PrivilegeLevel
from scrapli_community.vyos.vyos.async_driver import default_async_on_close, default_async_on_open
from scrapli_community.vyos.vyos.sync_driver import default_sync_on_close, default_sync_on_open

DEFAULT_PRIVILEGE_LEVELS = {
    "privilege_exec": (
        PrivilegeLevel(
            pattern=r"^[a-z0-9\.\--_()/:~]{1,1000}@[a-z0-9\.\--_()/:~]{1,1000}\$",
            name="privilege_exec",
            previous_priv="",
            deescalate="",
            escalate="",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
    "configuration": (
        PrivilegeLevel(
            pattern=r"^[a-z0-9\.\--_()/:~]{1,1000}@[a-z0-9\.\--_()/:~]{1,1000}#",
            name="configuration",
            previous_priv="privilege_exec",
            deescalate="exit",
            escalate="configure",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
}

SCRAPLI_PLATFORM = {
    "driver_type": "network",
    "defaults": {
        "privilege_levels": DEFAULT_PRIVILEGE_LEVELS,
        "default_desired_privilege_level": "privilege_exec",
        "sync_on_open": default_sync_on_open,
        "async_on_open": default_async_on_open,
        "sync_on_close": default_sync_on_close,
        "async_on_close": default_async_on_close,
        "comms_return_char": "\r\n",
        "failed_when_contains": [
            "Ambiguous command",
            "Incomplete command",
            "Invalid command",
            "Invalid value",
            "Need to specify the config node to set",
            "Set failed",
        ],
        "textfsm_platform": "",
        "genie_platform": "",
    },
}
