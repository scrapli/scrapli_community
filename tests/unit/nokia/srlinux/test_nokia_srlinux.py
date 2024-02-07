import re

import pytest

from scrapli_community.nokia.srlinux.nokia_srlinux import DEFAULT_PRIVILEGE_LEVELS


@pytest.mark.parametrize(
    "priv_pattern",
    [
        ("exec", "--{ running }--[  ]--\nA:srl#"),
        ("exec", "--{ + running }--[  ]--\nA:srl#"),
        ("exec", "--{ [YANG RELOAD] [FACTORY] running }--[  ]--\nA:r2# "),
        ("exec", "--{ [OLD STARTUP] running }--[  ]--\nA:r2# "),
        ("configuration", "--{ candidate shared-exclusive default }--[  ]--\nA:srl#"),
        ("configuration", "--{ candidate shared-exclusive default }--[ platform ]--\nA:srl#"),
        ("configuration", "--{ [FACTORY] candidate private private-root }--[  ]--\nA:r2# "),
        ("configuration", "--{ [FACTORY] * candidate private private-root }--[  ]--\nA:r2# "),
        ("configuration", "--{ + candidate shared default }--[  ]--\nA:r2# "),
    ],
    ids=[
        "exec",
        "exec_config_not_saved",
        "exec_factory_and_yang_reload",
        "exec_old_startup",
        "configuration",
        "configuration_with_path",
        "configuration_private",
        "configuration_uncommited_changes",
        "configuration_simple",
    ],
)
def test_default_prompt_patterns(priv_pattern):
    priv_level_name = priv_pattern[0]
    prompt = priv_pattern[1]

    prompt_pattern = DEFAULT_PRIVILEGE_LEVELS.get(priv_level_name).pattern
    match = re.search(pattern=prompt_pattern, string=prompt, flags=re.M | re.I)

    assert match
