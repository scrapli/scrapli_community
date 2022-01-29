import re

import pytest

from scrapli_community.cisco.cbs.cisco_cbs import DEFAULT_PRIVILEGE_LEVELS


@pytest.mark.parametrize(
    "priv_pattern",
    [
        ("exec", "SG250-08>"),
        ("privilege_exec", "SG250-08#"),
        ("privilege_exec", "a1234567890123456...#"),
        ("configuration", "SG250-08(config)#"),
        ("configuration", "SG250-08(config-if)#"),
        ("configuration", "a1234567890123456...(config)#"),
        ("configuration", "a1234567890123456...(config-if)#"),
    ],
    ids=[
        "ssh_prompt_exec",
        "ssh_prompt_privilege_exec",
        "ssh_prompt_privilege_exec",
        "ssh_prompt_configuration",
        "ssh_prompt_configuration",
        "ssh_prompt_configuration_interface",
        "ssh_prompt_configuration_interface",
    ],
)
def test_default_prompt_patterns(priv_pattern):
    priv_level_name = priv_pattern[0]
    prompt = priv_pattern[1]

    prompt_pattern = DEFAULT_PRIVILEGE_LEVELS.get(priv_level_name).pattern
    match = re.search(pattern=prompt_pattern, string=prompt, flags=re.M | re.I)

    assert match
