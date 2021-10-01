"""scrapli_community.cisco.asa.cisco_asa"""

from scrapli.driver.network.base_driver import PrivilegeLevel
from scrapli_community.cisco.asa.async_driver import default_async_on_close, default_async_on_open
from scrapli_community.cisco.asa.sync_driver import default_sync_on_close, default_sync_on_open

DEFAULT_PRIVILEGE_LEVELS = {
    "exec": (
        PrivilegeLevel(
            pattern=r"^[\S]{1,63}>$",
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
            pattern=r"^[\S]{1,63}#$",
            name="privilege_exec",
            previous_priv="exec",
            deescalate="disable",
            escalate="enable",
            escalate_auth=True,
            escalate_prompt=r"^(P|p)assword:\s?$",
        )
    ),
    "configuration": (
        PrivilegeLevel(
            pattern=r"^[\w.\-@\:]{1,63}\([\w.\-@\:+]{0,32}\)#$",
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
            "% Invalid input detected",
            "% Ambiguous command",
            "% Incomplete command",
        ],
        "textfsm_platform": "cisco_asa",
        "genie_platform": "asa",
    },
}
