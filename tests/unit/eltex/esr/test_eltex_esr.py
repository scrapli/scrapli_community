import re

import pytest

from scrapli_community.eltex.esr.eltex_esr import DEFAULT_PRIVILEGE_LEVELS


@pytest.mark.parametrize(
    "priv_pattern",
    [
        ("exec", "scrapli-esr-1> "),
        ("privilege_exec", "scrapli-esr-1# "),
        ("privilege_exec", "SCRAPLIESR# "),
        ("configuration", "scrapli-esr-1(config)# "),
        ("configuration", "scrapli-esr-1(config-if-gi)# "),
        ("configuration", "scrapli-esr-1(config-loopback)# "),
        ("configuration", "scrapli-esr-1(config-user)# "),
    ],
    ids=[
        "ssh_prompt_exec",
        "ssh_prompt_privilege_exec",
        "ssh_prompt_privilege_exec",
        "ssh_prompt_configuration",
        "ssh_prompt_configuration_interface",
        "ssh_prompt_configuration_loopback",
        "ssh_prompt_configuration_username",
    ],
)
def test_default_prompt_patterns(priv_pattern):
    priv_level_name = priv_pattern[0]
    prompt = priv_pattern[1]

    prompt_pattern = DEFAULT_PRIVILEGE_LEVELS.get(priv_level_name).pattern
    match = re.search(pattern=prompt_pattern, string=prompt, flags=re.M | re.I)

    assert match
