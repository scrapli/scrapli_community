"""scrapli_community.alcatel.aos.alcatel_aos"""

from scrapli_community.alcatel.aos.async_driver import default_async_on_close
from scrapli_community.alcatel.aos.sync_driver import default_sync_on_close

SCRAPLI_PLATFORM = {
    "driver_type": "generic",
    "defaults": {
        # Prompt can be anything, but best practice is to end with > or #
        "comms_prompt_pattern": r"^[a-zA-Z0-9.\-_@\/:]{1,63}[>|#]\s*",
        "sync_on_open": None,
        "async_on_open": None,
        "sync_on_close": default_sync_on_close,
        "async_on_close": default_async_on_close,
    },
}
