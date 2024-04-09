"""scrapli_community.hp.comware.hp_comware"""

from scrapli.driver.network.base_driver import PrivilegeLevel
from scrapli_community.hp.comware.async_driver import (
    AsyncHPComwareDriver,
    default_async_on_close,
    default_async_on_open,
)
from scrapli_community.hp.comware.sync_driver import (
    HPComwareDriver,
    default_sync_on_close,
    default_sync_on_open,
)

DEFAULT_PRIVILEGE_LEVELS = {
    "privilege_exec": (
        PrivilegeLevel(
            pattern=r"^<[a-z0-9.\-_@()/:]{1,48}>\s*$",
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
            pattern=r"^(?=\[[a-z0-9.\-_@/:]{1,64}\]$).*$",
            name="configuration",
            previous_priv="privilege_exec",
            deescalate="quit",
            escalate="system-view",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
}

SCRAPLI_PLATFORM = {
    "driver_type": {
        "sync": HPComwareDriver,
        "async": AsyncHPComwareDriver,
    },
    "defaults": {
        "privilege_levels": DEFAULT_PRIVILEGE_LEVELS,
        "default_desired_privilege_level": "privilege_exec",
        "sync_on_open": default_sync_on_open,
        "async_on_open": default_async_on_open,
        "sync_on_close": default_sync_on_close,
        "async_on_close": default_async_on_close,
        "failed_when_contains": [
            "% Unrecognized command found at '^' position.",
        ],
        "textfsm_platform": "hp_comware",
        "genie_platform": "",
        # Force the screen to be 256 characters wide.
        # Might get overwritten by global Scrapli transport options.
        # See issue #18 for more details.
        "transport_options": {"ptyprocess": {"cols": 256}},
    },
}
