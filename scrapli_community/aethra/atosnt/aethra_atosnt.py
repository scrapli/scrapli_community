"""scrapli_community.aethra.atosnt.aethra_atosnt"""

from scrapli_community.aethra.atosnt.async_diver import default_async_on_close
from scrapli_community.aethra.atosnt.sync_driver import default_sync_on_close

SCRAPLI_PLATFORM = {
    "driver_type": "generic",
    "defaults": {
        "comms_prompt_pattern": r"^[a-z0-9.\-_@]{1,64}>>",
        "sync_on_open": None,
        "async_on_open": None,
        "sync_on_close": default_sync_on_close,
        "async_on_close": default_async_on_close,
    },
}
