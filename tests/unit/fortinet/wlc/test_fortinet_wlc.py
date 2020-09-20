import re

import pytest

from scrapli_community.fortinet.wlc.fortinet_wlc import DEFAULT_PRIVILEGE_LEVELS


@pytest.mark.parametrize(
    "priv_pattern",
    [
        ("privilege_exec", "SCRAPLI-FORTINET-WLC-TEST(1)#"),
        ("configuration", "SCRAPLI-FORTINET-WLC-TEST(15)(config)#"),
        ("configuration", "SCRAPLI-FORTINET-WLC-TEST(15)(config-ap)#"),
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
