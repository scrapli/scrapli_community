import re

import pytest

from scrapli_community.siemens.roxii.siemens_roxii import DEFAULT_PRIVILEGE_LEVELS


@pytest.mark.parametrize(
    "priv_pattern",
    [
        ("privilege_exec", "SCRAPLI-SIEMENS-ROXII-TEST#"),
        ("configuration", "SCRAPLI-SIEMENS-ROXII-TEST(config)#"),
        ("configuration", "SCRAPLI-SIEMENS-ROXII-TEST(config-admin)#"),
    ],
    ids=[
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
