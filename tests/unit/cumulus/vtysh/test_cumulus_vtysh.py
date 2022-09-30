import re

import pytest

from scrapli_community.cumulus.vtysh.cumulus_vtysh import DEFAULT_PRIVILEGE_LEVELS


@pytest.mark.parametrize(
    "priv_pattern",
    [
        ("linux", "user@scrapli1-r01-test-location1:mgmt-vrf:~$"),
        ("linux", "root@scrapli1-r01-test-location1:mgmt-vrf:~#"),
        ("exec", "SCRAPLI-R1#"),
        ("configuration", "scrapli_r1(config)#"),
    ],
    ids=[
        "linux",
        "linux",
        "exec",
        "configuration",
    ],
)
def test_default_prompt_patterns(priv_pattern):
    priv_level_name = priv_pattern[0]
    prompt = priv_pattern[1]

    prompt_pattern = DEFAULT_PRIVILEGE_LEVELS.get(priv_level_name).pattern
    match = re.search(pattern=prompt_pattern, string=prompt, flags=re.M | re.I)

    assert match
