import re

import pytest

from scrapli_community.ruckus.unleashed.ruckus_unleashed import DEFAULT_PRIVILEGE_LEVELS


@pytest.mark.parametrize(
    "priv_pattern",
    [
        ("exec", "ruckus> "),
        ("exec", "anuc> "),
        ("privilege_exec", "ruckus# "),
        ("privilege_exec", "anuc# "),
        ("configuration", "ruckus(config)# "),
        ("configuration", "anuc(config)# "),
        ("configuration", "ruckus(config-sys-if)# "),
        ("configuration", "anuc(config-sys-if)# "),
        ("debug", "ruckus(debug)# "),
        ("debug", "anuc(debug)# "),
    ],
    ids=[
        "base_prompt_exec",
        "oem_anw_base_prompt_exec",
        "base_prompt_privilege_exec",
        "oem_anw_base_prompt_privilege_exec",
        "base_prompt_configuration",
        "oem_anw_base_prompt_configuration",
        "system_interface_configuration",
        "oem_anw_system_interface_configuration",
        "base_prompt_debug",
        "oem_anw_base_prompt_debug",
    ],
)
def test_default_prompt_patterns(priv_pattern):
    priv_level_name = priv_pattern[0]
    prompt = priv_pattern[1]
    prompt_pattern = DEFAULT_PRIVILEGE_LEVELS.get(priv_level_name).pattern
    match = re.search(pattern=prompt_pattern, string=prompt, flags=re.M | re.I)
    assert match
