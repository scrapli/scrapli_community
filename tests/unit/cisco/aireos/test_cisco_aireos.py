import re

import pytest

from scrapli_community.cisco.aireos.cisco_aireos import DEFAULT_PRIVILEGE_LEVELS




@pytest.mark.parametrize(
    "priv_pattern",
    [
        ("exec", "(Cisco Controller) >"),
        ("exec", "(something_fun) >"),
        ("configuration", "(Cisco Controller) config>"),
        ("configuration", "(Its interestin) config>"),
    ],
    ids=[
        "base_prompt_exec",
        "base_prompt_exec_non_default",
        "base_prompt_configuration",
        "base_prompt_configuration_non_default",
    ],
)
def test_default_prompt_patterns(priv_pattern):
    priv_level_name = priv_pattern[0]
    prompt = priv_pattern[1]
    prompt_pattern = DEFAULT_PRIVILEGE_LEVELS.get(priv_level_name).pattern
    match = re.search(pattern=prompt_pattern, string=prompt, flags=re.M | re.I)
    assert match
