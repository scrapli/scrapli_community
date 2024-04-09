"""scrapli_community.versa.flexvnf.versa_flexvnf"""

from scrapli.driver.network.base_driver import PrivilegeLevel
from scrapli_community.versa.flexvnf.async_driver import (
    default_async_on_close,
    default_async_on_open,
)
from scrapli_community.versa.flexvnf.sync_driver import default_sync_on_close, default_sync_on_open

DEFAULT_PRIVILEGE_LEVELS = {
    "shell": (
        PrivilegeLevel(
            pattern=r"^\[\w+\@\S+ \S+\] \$ ?$",
            name="shell",
            previous_priv="",
            deescalate="",
            escalate="cli",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
    "cli": (
        PrivilegeLevel(
            pattern=r"^\w+@\S+-cli> ?$",
            name="cli",
            previous_priv="shell",
            deescalate="exit",
            escalate="configure",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
    "configuration": (
        PrivilegeLevel(
            pattern=r"^\w+@\S+-cli\(\S+\)% ?$",
            name="configuration",
            previous_priv="cli",
            deescalate="exit",
            escalate="",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
}

SCRAPLI_PLATFORM = {
    "driver_type": "network",
    "defaults": {
        "privilege_levels": DEFAULT_PRIVILEGE_LEVELS,
        "default_desired_privilege_level": "cli",
        "sync_on_open": default_sync_on_open,
        "async_on_open": default_async_on_open,
        "sync_on_close": default_sync_on_close,
        "async_on_close": default_async_on_close,
        "failed_when_contains": ["[error]"],
        "textfsm_platform": "",
        "genie_platform": "",
    },
    "variants": {},
}
