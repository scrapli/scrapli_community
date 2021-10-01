import re

import pytest

from scrapli_community.cisco.aireos.cisco_aireos import DEFAULT_PRIVILEGE_LEVELS


# TODO
@pytest.mark.parametrize(
    "priv_pattern",
    [
        ("exec", "(Cisco Controller) >"),
        ("configuration", "(Cisco Controller) config>"),
    ],
    ids=[
        "base_prompt_exec",
        "base_prompt_configuration",
    ],
)
def test_default_prompt_patterns(priv_pattern):
    priv_level_name = priv_pattern[0]
    prompt = priv_pattern[1]
    prompt_pattern = DEFAULT_PRIVILEGE_LEVELS.get(priv_level_name).pattern
    match = re.search(pattern=prompt_pattern, string=prompt, flags=re.M | re.I)
    assert match
