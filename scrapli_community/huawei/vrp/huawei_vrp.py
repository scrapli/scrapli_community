"""scrapli_community.huawei.vrp.huawei_vrp"""

from scrapli.driver.network.base_driver import PrivilegeLevel
from scrapli_community.huawei.vrp.async_driver import (
    AsyncHuaweiVRPDriver,
    default_async_on_close,
    default_async_on_open,
)
from scrapli_community.huawei.vrp.sync_driver import (
    HuaweiVRPDriver,
    default_sync_on_close,
    default_sync_on_open,
)

DEFAULT_PRIVILEGE_LEVELS = {
    "privilege_exec": (
        PrivilegeLevel(
            pattern=r"^(?:hrp_[a|m|s])?<[a-z0-9.\-_@()/:]{1,48}>\s*$",
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
            # On some versions of VRP running on the AR160 & AR650 router series (and possibly
            # others), the router outputs the current OS version in the following format when
            # calling the command 'display current-configuration':
            #
            # <HOSTNAME>display current-configuration
            # [V200R009C00SPC500]
            # #
            # sysname HOSTNAME
            # ...
            #
            # Since the version string is basically in the same format as the prompt in
            # configuration mode, scrapli only reads until it sees this very string, and then
            # stops reading since it assumes that a valid prompt has been found.
            #
            # The following pattern tries to prevent this from happening by using a regex negative
            # lookahead to exclude '[V***R***C**]' from the prompt pattern, but still match
            # a regular hostname.
            #
            pattern=r"^(?!\[V\d{3}R\d{3}C\d{2,3}.*\])"
            r"(?=(?:hrp_[a|m|s])?\[\~{0,1}\*{0,1}[a-z0-9.\-_@/:]{1,64}\]$).*$",
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
        "sync": HuaweiVRPDriver,
        "async": AsyncHuaweiVRPDriver,
    },
    "defaults": {
        "privilege_levels": DEFAULT_PRIVILEGE_LEVELS,
        "default_desired_privilege_level": "privilege_exec",
        "sync_on_open": default_sync_on_open,
        "async_on_open": default_async_on_open,
        "sync_on_close": default_sync_on_close,
        "async_on_close": default_async_on_close,
        "failed_when_contains": [
            "Error:",
        ],
        "textfsm_platform": "huawei_vrp",
        "genie_platform": "",
        # Force the screen to be 256 characters wide.
        # Might get overwritten by global Scrapli transport options.
        # See issue #18 for more details.
        "transport_options": {"ptyprocess": {"cols": 256}},
    },
}
