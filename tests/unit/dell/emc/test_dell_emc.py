import re

import pytest

from scrapli_community.dell.emc.dell_emc import DEFAULT_PRIVILEGE_LEVELS


@pytest.mark.parametrize(
    "priv_pattern",
    [
        ("exec", "SCRAPLI_DELL-TEST_SW>"),
        ("privilege_exec", "SCRAPLI_DELL-TEST_SW#"),
        ("configuration", "SCRAPLI_DELL-TEST_SW(config)#"),
        ("configuration", "SCRAPLI_DELL-TEST_SW(config-if-Gi1/0/1)#"),
    ],
    ids=[
        "ssh_prompt_exec",
        "ssh_prompt_privilege_exec",
        "ssh_prompt_configuration",
        "ssh_prompt_configuration_interface",
    ],
)
def test_default_prompt_patterns(priv_pattern):
    priv_level_name = priv_pattern[0]
    prompt = priv_pattern[1]
    prompt_pattern = DEFAULT_PRIVILEGE_LEVELS.get(priv_level_name).pattern
    match = re.search(pattern=prompt_pattern, string=prompt, flags=re.M | re.I)
    assert match
