"""scrapli_community.ruckus.unleashed.ruckus_unleashed"""

from scrapli.driver.network.base_driver import PrivilegeLevel
from scrapli_community.ruckus.unleashed.async_driver import (
    default_async_on_close,
    default_async_on_open,
)
from scrapli_community.ruckus.unleashed.sync_driver import (
    default_sync_on_close,
    default_sync_on_open,
)

DEFAULT_PRIVILEGE_LEVELS = {
    "exec": (
        PrivilegeLevel(
            pattern=r"^[a-z0-9]{1,24}>\s*$",
            name="exec",
            previous_priv="",
            deescalate="",
            escalate="",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
    "setup_wizard": (
        PrivilegeLevel(
            pattern=r"^[a-z ?]{1,48}\[yes/no\]:\s*$",
            name="setup_wizard",
            previous_priv="exec",
            deescalate="no",
            escalate="",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
    "privilege_exec": (
        PrivilegeLevel(
            pattern=r"^[a-z0-9]{1,24}#\s*$",
            name="privilege_exec",
            previous_priv="exec",
            deescalate="disable",
            escalate="enable force",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
    "configuration": (
        PrivilegeLevel(
            pattern=r"^[a-z0-9]{1,24}\(conf[a-z0-9\-]{0,24}\)#\s*$",
            name="configuration",
            previous_priv="privilege_exec",
            deescalate="end",
            escalate="config",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
    "debug": (
        PrivilegeLevel(
            pattern=r"^[a-z0-9]{1,24}\(debug\)#\s*$",
            name="debug",
            previous_priv="privilege_exec",
            deescalate="quit",
            escalate="debug",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
    "ap_mode": (
        PrivilegeLevel(
            pattern=r"^[a-z0-9]{1,24}\(ap-mode\)#\s*$",
            name="ap_mode",
            previous_priv="privilege_exec",
            deescalate="quit",
            escalate="ap-mode",
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
            "The command is",
            "is invalid",
            "must consist",
        ],
        "textfsm_platform": "",
        "genie_platform": "",
        "auth_bypass": True,
    },
}
