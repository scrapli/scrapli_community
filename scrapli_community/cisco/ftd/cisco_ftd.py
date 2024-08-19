"""
scrapli_community.cisco.ftd.cisco_ftd

Welcome to infamous FTD CLI driver!
If you are so desperate to run this code, you have to know a couple of things:

* Always use full words for commands!
  Otherwise, your connection will stall because FTD tries to complete it and it confuses Scrapli
  logic.
  E.g.: DO NOT do this: conn.send_command("show run"), instead:
  conn.send_command("show running-config")

* Do not use CLI filters without testing first!
  Commands like: show failover | include This host:.*Active
  might fail because prompt is handled strangely by FTD. In this case, just do not filter on the
  CLI but in your code.
  Filters are buggy anyway: simple regex expressions don't work. E.g. parentheses.
  In the worst case, set `eager` to True.

* If you want to run commands in expert/root mode, you need to specify desired_privilege_level by
 connection data and
  specify auth_secondary (admin password)!
  data = {
    "host": "172.18.0.11",
    "platform": "cisco_ftd",
    "auth_username": "scrapli",
    "auth_password": "scrapli",
    "auth_secondary": "scrapli",
    "auth_strict_key": False,
    #"default_desired_privilege_level": "root",  # only use this if you want to run linux commands!
  }
  with Scrapli(**data) as conn:
    ...

"""

from scrapli.driver.network.base_driver import PrivilegeLevel
from scrapli_community.cisco.ftd.async_driver import default_async_on_close, default_async_on_open
from scrapli_community.cisco.ftd.sync_driver import default_sync_on_close, default_sync_on_open

DEFAULT_PRIVILEGE_LEVELS = {
    "exec": (
        PrivilegeLevel(
            pattern=r"^>\s*",
            name="exec",
            previous_priv="",
            deescalate="",
            escalate="",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
    "expert": (
        PrivilegeLevel(
            pattern=r"^[\w.-]{1,63}@[^$]+\$\s*$",
            name="expert",
            previous_priv="exec",
            deescalate="exit",
            escalate="expert",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
    "root": (
        PrivilegeLevel(
            pattern=r"^root@[^#]+#\s*$",
            name="root",
            previous_priv="expert",
            deescalate="exit",
            escalate="sudo su -",
            escalate_auth=True,
            escalate_prompt="Password:",
        )
    ),
}

SCRAPLI_PLATFORM = {
    "driver_type": "network",
    "defaults": {
        "privilege_levels": DEFAULT_PRIVILEGE_LEVELS,
        "default_desired_privilege_level": "exec",  # set this by connection data if needed
        "sync_on_open": default_sync_on_open,
        "async_on_open": default_async_on_open,
        "sync_on_close": default_sync_on_close,
        "async_on_close": default_async_on_close,
        "failed_when_contains": [
            "Syntax error:",
        ],
        "textfsm_platform": "cisco_ftd",  # hardly supported, don't count on it
        # "genie_platform": "ftd",  # not supported
    },
}
