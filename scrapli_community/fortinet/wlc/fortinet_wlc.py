"""scrapli_community.fortinet.wlc.fortinet_wlc"""
from scrapli.driver.network.base_driver import PrivilegeLevel

from scrapli_community.fortinet.wlc._async import default_async_on_close, default_async_on_open
from scrapli_community.fortinet.wlc.sync import default_sync_on_close, default_sync_on_open

DEFAULT_PRIVILEGE_LEVELS = {
    "privilege_exec": (
        PrivilegeLevel(
            pattern=r"^[a-z0-9-]{1,48}\(\d{1,2}\)#\s*$",
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
            pattern=r"^[a-z0-9-]{1,48}\(\d{1,2}\)\(conf[a-z0-9.\-@/:\+]{0,32}\)#\s*$",
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
            "is not unique",
            "Unrecognized command",
            "Insufficient parameters for command",
            "Error:",
        ],
        "textfsm_platform": "",
        "genie_platform": "",
    },
}
