import re

import pytest

from scrapli_community.cumulus.linux.cumulus_linux import DEFAULT_PRIVILEGE_LEVELS


@pytest.mark.parametrize(
    "priv_pattern",
    [
        ("exec", "user@scrapli1-r01-test-location1:mgmt-vrf:~$"),
        ("configuration", "root@SCRAPLI1-R01-TEST-LOCATION1:MGMT-VRF:~#"),
        ("configuration", "root@scrapli1_r01_test-location1:mgmt-vrf:/home/user#"),
    ],
    ids=[
        "exec",
        "configuration",
        "configuration_after_su",
    ],
)
def test_default_prompt_patterns(priv_pattern):
    priv_level_name = priv_pattern[0]
    prompt = priv_pattern[1]

    prompt_pattern = DEFAULT_PRIVILEGE_LEVELS.get(priv_level_name).pattern
    match = re.search(pattern=prompt_pattern, string=prompt, flags=re.M | re.I)

    assert match
