"""scrapli_community.cumulus.linux.cumulus_linux"""

from scrapli.driver.network.base_driver import PrivilegeLevel
from scrapli_community.cumulus.linux.async_driver import (
    default_async_on_close,
    default_async_on_open,
)
from scrapli_community.cumulus.linux.sync_driver import default_sync_on_close, default_sync_on_open

DEFAULT_PRIVILEGE_LEVELS = {
    "exec": (
        PrivilegeLevel(
            pattern=r"^\S+@\S+:\S+:\S+\$\s*$",
            name="exec",
            previous_priv="",
            deescalate="",
            escalate="",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
    "configuration": (
        PrivilegeLevel(
            pattern=r"^\S+@\S+:\S+:\S+#\s*$",
            name="configuration",
            previous_priv="exec",
            deescalate="exit",
            escalate="sudo su",
            escalate_auth=True,
            escalate_prompt=": ",
        )
    ),
}

LOGIN_AS_ROOT = {
    "exec": (
        PrivilegeLevel(
            pattern=r"^\S+@\S+:\S+:\S+#\s*$",
            name="exec",
            previous_priv="",
            deescalate="",
            escalate="",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
    "configuration": (
        PrivilegeLevel(
            pattern=r"^\S+@\S+:\S+:\S+#\s*$",
            name="configuration",
            previous_priv="exec",
            deescalate="",
            escalate="",
            escalate_auth=False,
            escalate_prompt=": ",
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
        ],
        "textfsm_platform": "",
        "genie_platform": "",
    },
    "variants": {
        "root-login": {
            "privilege_levels": LOGIN_AS_ROOT,
            "sync_on_open": default_sync_on_open,
            "async_on_open": default_async_on_open,
            "sync_on_close": default_sync_on_close,
            "async_on_close": default_async_on_close,
            "failed_when_contains": [
                "Permission denied",
                "ERROR:",
            ],
            "textfsm_platform": "",
            "genie_platform": "",
        }
    },
}
