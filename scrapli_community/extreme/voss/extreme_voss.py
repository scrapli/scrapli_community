"""scrapli_community.extreme.voss.extreme_voss"""

from scrapli.driver.network.base_driver import PrivilegeLevel
from scrapli_community.extreme.voss.async_driver import default_async_on_close, default_async_on_open
from scrapli_community.extreme.voss.sync_driver import default_sync_on_close, default_sync_on_open

DEFAULT_PRIVILEGE_LEVELS = {
    "exec": (
        PrivilegeLevel(
            pattern=r"^\[\w. -]{1,255}:\d+>$",
            name="exec",
            previous_priv="",
            deescalate="",
            escalate="",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
        "privilege_exec": (
        PrivilegeLevel(
            pattern=r"^\[\w. -]{1,255}:\d+#$",
            name="privilege_exec",
            previous_priv="exec",
            deescalate="disable",
            escalate="enable",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
    "configuration": (
        PrivilegeLevel(
            pattern=r"^\[\w. -]{1,255}:\d+ \(config\)#$",
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
        "failed_when_contains": [
            "% Invalid input detected",
            "% Ambiguous command",
            "% Incomplete command",
        ],
        "textfsm_platform": "extreme_voss",
        "genie_platform": "voss",
    },
    "variants": {
        "read_only": {
            # Warning: terminal width may be default 80 which can interfere parsing!
            # useful for users without config mode privilege
            "sync_on_open": read_only_sync_on_open,
            "async_on_open": read_only_async_on_open,
        }
    },
}
