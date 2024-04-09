"""scrapli_community.datacom.dmos.datacom_dmos"""

from scrapli.driver.network.base_driver import PrivilegeLevel
from scrapli_community.datacom.dmos.async_driver import (
    AsyncDatacomDmosDriver,
    default_async_on_close,
    default_async_on_open,
)
from scrapli_community.datacom.dmos.sync_driver import (
    DatacomDmosDriver,
    default_sync_on_close,
    default_sync_on_open,
)

DEFAULT_PRIVILEGE_LEVELS = {
    "exec": (
        PrivilegeLevel(
            pattern=r"^[\w\.\-]+#\s*$",
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
            pattern=r"^[\w\.\-]+\(config\)#\s*$",
            name="configuration",
            previous_priv="exec",
            deescalate="exit",
            escalate="config terminal",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
}

SCRAPLI_PLATFORM = {
    "driver_type": {
        "sync": DatacomDmosDriver,
        "async": AsyncDatacomDmosDriver,
    },
    "defaults": {
        "privilege_levels": DEFAULT_PRIVILEGE_LEVELS,
        "default_desired_privilege_level": "exec",
        "sync_on_open": default_sync_on_open,
        "async_on_open": default_async_on_open,
        "sync_on_close": default_sync_on_close,
        "async_on_close": default_async_on_close,
        "failed_when_contains": [
            "Error:",
        ],
        "textfsm_platform": "",
        "genie_platform": "",
        # Force the screen to be 256 characters wide.
        # Might get overwritten by global Scrapli transport options.
        # See issue #18 for more details.
        "transport_options": {"ptyprocess": {"cols": 256}},
    },
}
