"""scrapli_community.edgecore.ecs.edgecore_ecs"""
from scrapli.driver.network.base_driver import PrivilegeLevel

from scrapli_community.edgecore.ecs._async import default_async_on_close, default_async_on_open
from scrapli_community.edgecore.ecs.sync import default_sync_on_close, default_sync_on_open

DEFAULT_PRIVILEGE_LEVELS = {
    "privilege_exec": (
        PrivilegeLevel(
            pattern=r"^[a-z0-9.\-_@()/:]{1,48}#\s*$",
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
            pattern=r"^[a-z0-9.\-_@/:]{1,63}\(conf[a-z0-9.\-@/:\+]{0,32}\)#$",
            name="configuration",
            previous_priv="privilege_exec",
            deescalate="end",
            escalate="conf",
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
            "% Ambiguous command",
            "% Incomplete command",
            "% Invalid input detected",
            "% Unknown command",
        ],
        "textfsm_platform": "",
        "genie_platform": "",
    },
}
