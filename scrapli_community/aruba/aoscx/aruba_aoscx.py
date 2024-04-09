"""scrapli_community.aruba.aoscx.aruba_aoscx"""

from scrapli.driver.network.base_driver import PrivilegeLevel
from scrapli_community.aruba.aoscx.async_driver import default_async_on_close, default_async_on_open
from scrapli_community.aruba.aoscx.sync_driver import default_sync_on_close, default_sync_on_open

DEFAULT_PRIVILEGE_LEVELS = {
    "privilege_exec": (
        PrivilegeLevel(
            pattern=r"^[\w.\-@/:]{1,63}#\s?$",
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
            pattern=r"^[\w.\-@/:]{1,63}\(config[\w.\-@/:]{0,32}\)#\s?$",
            name="configuration",
            previous_priv="privilege_exec",
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
        "default_desired_privilege_level": "privilege_exec",
        "sync_on_open": default_sync_on_open,
        "async_on_open": default_async_on_open,
        "sync_on_close": default_sync_on_close,
        "async_on_close": default_async_on_close,
        "failed_when_contains": ["% Command incomplete.", "Invalid input:", "doesn't exist"],
        "textfsm_platform": "aruba_aoscx",
        "genie_platform": "",
    },
    "variants": {},
}
