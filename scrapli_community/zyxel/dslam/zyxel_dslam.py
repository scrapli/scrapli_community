"""scrapli_community.zyxel.dslam.zyxel_dslam"""

from scrapli.driver.network.base_driver import PrivilegeLevel
from scrapli_community.zyxel.dslam.async_driver import (
    AsyncZyxelDSLAMDriver,
    default_async_on_close,
    default_async_on_open,
)
from scrapli_community.zyxel.dslam.sync_driver import (
    ZyxelDSLAMDriver,
    default_sync_on_close,
    default_sync_on_open,
)

DEFAULT_PRIVILEGE_LEVELS = {
    "exec": (
        PrivilegeLevel(
            pattern=r"^(.*)[a-zA-Z0-9_\-]*[\>#]\s*$",
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
    "driver_type": {
        "sync": ZyxelDSLAMDriver,
        "async": AsyncZyxelDSLAMDriver,
    },
    "defaults": {
        "privilege_levels": DEFAULT_PRIVILEGE_LEVELS,
        "default_desired_privilege_level": "exec",
        "sync_on_open": default_sync_on_open,
        "async_on_open": default_async_on_open,
        "sync_on_close": default_sync_on_close,
        "async_on_close": default_async_on_close,
        "timeout_ops": 300,
        "failed_when_contains": [
            "invalid command",
            "command authorization fail",
        ],
        "textfsm_platform": "zyxel_dslam",
        "genie_platform": "",
    },
}
