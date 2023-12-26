"""scrapli_community.cisco.aireos.cisco_aireos"""

from scrapli.driver.network.base_driver import PrivilegeLevel
from scrapli_community.cisco.aireos.async_driver import (
    default_async_on_close,
    default_async_on_open,
)
from scrapli_community.cisco.aireos.sync_driver import default_sync_on_close, default_sync_on_open

DEFAULT_PRIVILEGE_LEVELS = {
    "exec": (
        PrivilegeLevel(
            pattern=r"^\([\w. -]{1,31}\) >$",
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
            pattern=r"^\([\w. -]{1,31}\) config>$",
            name="configuration",
            previous_priv="exec",
            deescalate="exit",
            escalate="config",
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
            "Incorrect Usage. Use the '?' or <TAB> key to list commands.",
            "Incorrect input!",
        ],
        "textfsm_platform": "cisco_wlc_ssh",
        "genie_platform": "",
        "auth_bypass": True,
    },
}
