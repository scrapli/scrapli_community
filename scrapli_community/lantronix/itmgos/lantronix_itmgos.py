"""scrapli_community.lantronix.itmgos.lantronix_itmgos"""

from scrapli.driver.network.base_driver import PrivilegeLevel
from scrapli_community.lantronix.itmgos.async_driver import (
    default_async_on_close,
    default_async_on_open,
)
from scrapli_community.lantronix.itmgos.sync_driver import (
    default_sync_on_close,
    default_sync_on_open,
)

# IT Management Gateway OS (SLC 9000, SLC 8000, EMG 7500/8500, SLB) has one flat CLI
# with no enable or configuration mode. The prompt is the hostname in brackets: [slc-01]>
DEFAULT_PRIVILEGE_LEVELS = {
    "exec": (
        PrivilegeLevel(
            pattern=r"^\[[\w.\-]{1,64}\]>\s?$",
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
            "Unknown parameter",
            "Invalid number of parameters",
            "Invalid option",
            "Incomplete Command",
        ],
        "textfsm_platform": "lantronix_itmgos",
        "genie_platform": "",
    },
}
