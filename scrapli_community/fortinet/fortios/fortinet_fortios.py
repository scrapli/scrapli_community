"""scrapli_community.fortinet.wlc.fortinet_wlc"""

from scrapli_community.fortinet.fortios.async_driver import (
    AsyncFortinetFortiOSDriver,
    default_async_on_close,
    default_async_on_open,
)
from scrapli_community.fortinet.fortios.sync_driver import (
    FortinetFortiOSDriver,
    default_sync_on_close,
    default_sync_on_open,
)

SCRAPLI_PLATFORM = {
    "driver_type": {
        "sync": FortinetFortiOSDriver,
        "async": AsyncFortinetFortiOSDriver,
    },
    "defaults": {
        "comms_prompt_pattern": r"[\w_-]+ (\([\w-]+\) )?[$#]",
        "sync_on_open": default_sync_on_open,
        "async_on_open": default_async_on_open,
        "sync_on_close": default_sync_on_close,
        "async_on_close": default_async_on_close,
    },
}
