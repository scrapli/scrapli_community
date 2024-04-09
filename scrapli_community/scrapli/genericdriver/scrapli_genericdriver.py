"""scrapli_community.scrapli.genericdriver.scrapli_example"""

from scrapli_community.scrapli.genericdriver.async_driver import (
    default_async_on_close,
    default_async_on_open,
)
from scrapli_community.scrapli.genericdriver.sync_driver import (
    default_sync_on_close,
    default_sync_on_open,
)

SCRAPLI_PLATFORM = {
    "driver_type": "generic",
    "defaults": {
        "comms_prompt_pattern": r"^\(Cisco Controller\) >$",
        "sync_on_open": default_sync_on_open,
        "async_on_open": default_async_on_open,
        "sync_on_close": default_sync_on_close,
        "async_on_close": default_async_on_close,
        "auth_bypass": True,
    },
    "variants": {
        # just as an networkdriver... this won't do anything different than "normal" defaults as
        # above but this is how we can override the defaults
        "test_variant1": {"comms_prompt_pattern": r"^\(BLAH\) >$"}
    },
}
