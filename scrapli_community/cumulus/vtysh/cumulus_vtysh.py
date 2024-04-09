"""scrapli_community.cumulus.vtysh.cumulus_vtysh"""

from scrapli.driver.network.base_driver import PrivilegeLevel
from scrapli_community.cumulus.vtysh.async_driver import (
    default_async_on_close,
    default_async_on_open,
)
from scrapli_community.cumulus.vtysh.sync_driver import default_sync_on_close, default_sync_on_open

DEFAULT_PRIVILEGE_LEVELS = {
    "linux": (
        PrivilegeLevel(
            pattern=r"^\S+@\S+:\S+:\S+[\$|#]\s*$",
            name="linux",
            previous_priv="",
            deescalate="",
            escalate="",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
    "exec": (
        PrivilegeLevel(
            pattern=r"^[\w\.\-]+#\s*$",
            name="exec",
            previous_priv="linux",
            deescalate="exit",
            escalate="vtysh",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
    "configuration": (
        PrivilegeLevel(
            pattern=r"^[\w\.\-]+\(config\)#\s*$",
            name="configuration",
            previous_priv="exec",
            deescalate="exit",
            escalate="configure terminal",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
}


SCRAPLI_PLATFORM = {
    "driver_type": "network",
    "defaults": {
        "privilege_levels": DEFAULT_PRIVILEGE_LEVELS,
        "default_desired_privilege_level": "exec",
        "sync_on_open": default_sync_on_open,
        "async_on_open": default_async_on_open,
        "sync_on_close": default_sync_on_close,
        "async_on_close": default_async_on_close,
        "failed_when_contains": [
            "Permission denied",
            "ERROR:",
            "% Unknown command.",
            "% Command incomplete.",
        ],
        "textfsm_platform": "",
        "genie_platform": "",
    },
    "variants": {},
}
