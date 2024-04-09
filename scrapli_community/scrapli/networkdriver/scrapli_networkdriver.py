"""scrapli_community.scrapli.networkdriver.scrapli_example"""

from scrapli.driver.network.base_driver import PrivilegeLevel
from scrapli_community.scrapli.networkdriver.async_driver import (
    AsyncScrapliNetworkDriverWithMethods,
    default_async_on_close,
    default_async_on_open,
)
from scrapli_community.scrapli.networkdriver.sync_driver import (
    ScrapliNetworkDriverWithMethods,
    default_sync_on_close,
    default_sync_on_open,
)

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
            deescalate="disable",
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
        "failed_when_contains": [
            "% Ambiguous command",
            "% Incomplete command",
            "% Invalid input detected",
            "% Unknown command",
        ],
        "textfsm_platform": "cisco_iosxe",
        "genie_platform": "iosxe",
    },
    "variants": {
        # just as an networkdriver... this won't do anything different than "normal" defaults as
        # above but this is how we can override the defaults
        "test_variant1": {"default_desired_privilege_level": "configuration"},
        # test variant for testing instantiating a scrapli community platform class
        "test_variant2": {
            "driver_type": {
                "sync": ScrapliNetworkDriverWithMethods,
                "async": AsyncScrapliNetworkDriverWithMethods,
            },
        },
    },
}
