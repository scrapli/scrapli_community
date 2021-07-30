import re

import pytest

from scrapli_community.nokia.srlinux.nokia_srlinux import DEFAULT_PRIVILEGE_LEVELS


@pytest.mark.parametrize(
    "priv_pattern",
    [
        ("exec", "--{ running }--[  ]--\nA:srl#"),
        ("configuration", "--{ candidate shared-exclusive default }--[  ]--\nA:srl#"),
        ("configuration", "--{ candidate shared-exclusive default }--[ platform ]--\nA:srl#"),
    ],
    ids=[
        "exec",
        "configuration",
        "configuration_with_path",
    ],
)
def test_default_prompt_patterns(priv_pattern):
    priv_level_name = priv_pattern[0]
    prompt = priv_pattern[1]

    prompt_pattern = DEFAULT_PRIVILEGE_LEVELS.get(priv_level_name).pattern
    match = re.search(pattern=prompt_pattern, string=prompt, flags=re.M | re.I)

    assert match
