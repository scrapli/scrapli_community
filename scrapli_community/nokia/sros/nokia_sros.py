"""scrapli_community.nokia.sros.nokia_sros"""

from scrapli.driver.network.base_driver import PrivilegeLevel
from scrapli_community.nokia.sros.async_driver import (
    classic_aram_async_on_open,
    classic_default_async_on_open,
    default_async_on_close,
    default_async_on_open,
)
from scrapli_community.nokia.sros.sync_driver import (
    classic_aram_sync_on_open,
    classic_default_sync_on_open,
    default_sync_on_close,
    default_sync_on_open,
)

DEFAULT_PRIVILEGE_LEVELS = {
    "exec": (
        PrivilegeLevel(
            pattern=r"^(?!\(ex\)|\(ro\)|\(gl\)|\(pr\))\[.*\]\n[abcd]:[\w\._]+@[\w\s_.-]+#\s?$",
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
            pattern=r"^(?:!|\*)?\((ex|ex:bof)\)\[\/?\]\n\*?[abcd]:[\w\._]+@[\w\s_.-]+#\s?$",
            name="configuration",
            previous_priv="exec",
            deescalate="quit-config",
            escalate="edit-config exclusive",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
    "configuration_with_path": (
        PrivilegeLevel(
            pattern=r"^(?:!|\*)?\((ex|ex:bof)\)\[(\S|\s){2,}\]\n\*?[abcd]:[\w\._]+@[\w\s_.-]+#\s?$",
            name="configuration_with_path",
            previous_priv="exec",
            deescalate="exit all",
            escalate="",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
}

CLASSIC_DEFAULT_PRIVILEGE_LEVELS = {
    "exec": (
        PrivilegeLevel(
            pattern=r"^\*?[abcd]:[\w\s_.-]+#\s?$",
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
            pattern=r"^\*?[abcd]:[\w\s_.-]+>config[\w>]*(#|\$)\s?$",
            name="configuration",
            previous_priv="exec",
            deescalate="exit all",
            escalate="configure",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
}

CLASSIC_ARAM_PRIVILEGE_LEVELS = {
    "exec": (
        PrivilegeLevel(
            pattern=r"^(.*)[a-zA-Z0-9_\:\-\>]*[\#\$] ?$",
            name="exec",
            previous_priv="",
            deescalate="",
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
        "default_desired_privilege_level": "exec",
        "sync_on_open": default_sync_on_open,
        "async_on_open": default_async_on_open,
        "sync_on_close": default_sync_on_close,
        "async_on_close": default_async_on_close,
        "failed_when_contains": [
            "MINOR:",
            "MAJOR:",
        ],
        "textfsm_platform": "",
        "genie_platform": "",
    },
    "variants": {
        "classic": {
            "privilege_levels": CLASSIC_DEFAULT_PRIVILEGE_LEVELS,
            "sync_on_open": classic_default_sync_on_open,
            "async_on_open": classic_default_async_on_open,
            "failed_when_contains": [
                "MINOR:",
                "MAJOR:",
                "Error:",
                "Bad Command:",
            ],
        },
        "aram": {
            "privilege_levels": CLASSIC_ARAM_PRIVILEGE_LEVELS,
            "sync_on_open": classic_aram_sync_on_open,
            "async_on_open": classic_aram_async_on_open,
            "timeout_ops": 300,
            "failed_when_contains": [
                "command is not complete",
                "invalid token",
            ],
        },
    },
}
