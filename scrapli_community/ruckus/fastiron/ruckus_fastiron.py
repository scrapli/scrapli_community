"""scrapli_community.ruckus.fastiron.ruckus_fastiron"""
from scrapli.driver.network.base_driver import PrivilegeLevel

from scrapli_community.ruckus.fastiron._async import default_async_on_close, default_async_on_open
from scrapli_community.ruckus.fastiron.sync import default_sync_on_close, default_sync_on_open

DEFAULT_PRIVILEGE_LEVELS = {
    "exec": (
        PrivilegeLevel(
            pattern=r"^[a-z0-9.\-_@()/:]{1,63}>$",
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
            pattern=r"^[a-z0-9.\-_@/:]{1,63}#$",
            name="privilege_exec",
            previous_priv="exec",
            deescalate="quit",
            escalate="enable",
            escalate_auth=True,
            escalate_prompt=r"^[pP]assword:\s?$",
        )
    ),
    "configuration": (
        PrivilegeLevel(
            pattern=r"^[a-z0-9.\-_@/:]{1,63}\(conf[a-z0-9.\-@/:\+]{0,32}\)#$",
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
        "failed_when_contains": ["Error -", "Invalid input -"],
        "textfsm_platform": "brocade_fastiron",
        "genie_platform": "",
    },
    "variants": {},
}
