"""scrapli_community.cisco.cbs.cisco_cbs"""

from scrapli.driver.network.base_driver import PrivilegeLevel
from scrapli_community.cisco.cbs.async_driver import default_async_on_close, default_async_on_open
from scrapli_community.cisco.cbs.sync_driver import default_sync_on_close, default_sync_on_open

DEFAULT_PRIVILEGE_LEVELS = {
    "exec": (
        PrivilegeLevel(
            pattern=r"^[a-zA-Z0-9-.]{1,58}>$",
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
            pattern=r"^[a-zA-Z0-9-.]{1,58}#$",
            name="privilege_exec",
            previous_priv="exec",
            deescalate="disable",
            escalate="enable",
            escalate_auth=True,
            escalate_prompt=r"^(?:enable\s){0,1}Password:\s?$",
        )
    ),
    "configuration": (
        PrivilegeLevel(
            pattern=r"^[a-zA-Z0-9-.]{1,58}\([\w.\-@/:+]{1,32}\)#$",
            name="configuration",
            previous_priv="privilege_exec",
            deescalate="end",
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
            "% Incomplete command",
            "% Unrecognized command",
            "% missing mandatory parameter",
            "% bad parameter value",
            "% Ambiguous command",
        ],
        "textfsm_platform": "cisco_s300",
        "genie_platform": "",
    },
}
