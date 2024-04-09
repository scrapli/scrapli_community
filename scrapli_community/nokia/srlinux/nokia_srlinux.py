"""scrapli_community.nokia.srlinux.nokia_srlinux"""

from scrapli.driver.network.base_driver import PrivilegeLevel
from scrapli_community.nokia.srlinux.async_driver import (
    default_async_on_close,
    default_async_on_open,
)
from scrapli_community.nokia.srlinux.sync_driver import default_sync_on_close, default_sync_on_open

DEFAULT_PRIVILEGE_LEVELS = {
    # https://regex101.com/r/PGLSJJ/1
    "exec": (
        PrivilegeLevel(
            pattern=r"^--{(\s\[[\w\s]+\]){0,5}[\+\*\s]{1,}running\s}"
            r"--\[.+?\]--\s*\n[abcd]:\S+#\s*$",
            name="exec",
            previous_priv="",
            deescalate="",
            escalate="",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
    # https://regex101.com/r/JsaUZy/1
    "configuration": (
        PrivilegeLevel(
            pattern=r"^--{(\s\[[\w\s]+\]){0,5}[\+\*\!\s]{1,}candidate"
            r"[\-\w\s]+}--\[.+?\]--\s*\n[abcd]:\S+#\s*$",
            name="configuration",
            previous_priv="exec",
            deescalate="discard now",
            escalate="enter candidate exclusive",
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
            "MINOR:",
            "MAJOR:",
            "CRITICAL:",
        ],
        "textfsm_platform": "",
        "genie_platform": "",
    },
    "variants": {},
}
