"""scrapli_community.eltex.esr.exltex_esr"""
from scrapli.driver.network.base_driver import PrivilegeLevel

from scrapli_community.eltex.esr._async import default_async_on_close, default_async_on_open
from scrapli_community.eltex.esr.sync import default_sync_on_close, default_sync_on_open

DEFAULT_PRIVILEGE_LEVELS = {
    "exec": (
        PrivilegeLevel(
            pattern=r"^(\\n)?[a-z0-9.\-_@/:]{1,63}>\s*$",
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
            pattern=r"^(\\n)?[a-z0-9.\-_@/:]{1,63}#\s*$",
            name="privilege_exec",
            previous_priv="exec",
            deescalate="",
            escalate="enable",
            escalate_auth=True,
            escalate_prompt=r"^\s*[pP]assword:\s*$",
        )
    ),
    "configuration": (
        PrivilegeLevel(
            pattern=r"^(\\n)?[a-z0-9.\-_@/:]{1,63}\(conf[a-z0-9.\-@/:\+]{0,32}\)#\s*$",
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
    "driver_type": "network",  # generic|network
    "defaults": {
        "privilege_levels": DEFAULT_PRIVILEGE_LEVELS,
        "default_desired_privilege_level": "privilege_exec",
        "sync_on_open": default_sync_on_open,
        "async_on_open": default_async_on_open,
        "sync_on_close": default_sync_on_close,
        "async_on_close": default_async_on_close,
        "failed_when_contains": ["Syntax error: Illegal command line"],
        "textfsm_platform": "",
        "genie_platform": "",
    },
}
