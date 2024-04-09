"""scrapli_community.mikrotik.routeros.mikrotik_routeros"""

from scrapli_community.mikrotik.routeros.async_driver import (
    AsyncMikrotikRouterOSDriver,
    default_async_on_close,
)
from scrapli_community.mikrotik.routeros.sync_driver import (
    MikrotikRouterOSDriver,
    default_sync_on_close,
)

SCRAPLI_PLATFORM = {
    "driver_type": {
        "sync": MikrotikRouterOSDriver,
        "async": AsyncMikrotikRouterOSDriver,
    },
    "defaults": {
        "comms_prompt_pattern": r"\[[a-z0-9@.\-_+\s]{1,48}@[a-z0-9.\-_\s]{1,64}\].{1,16}>",
        "comms_return_char": "\r\n",  # Mikrotik ROS uses '\r\n' as newline character.
        "sync_on_open": None,
        "async_on_open": None,
        "sync_on_close": default_sync_on_close,
        "async_on_close": default_async_on_close,
    },
}
