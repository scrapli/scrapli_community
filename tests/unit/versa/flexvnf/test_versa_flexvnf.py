import re

import pytest

from scrapli_community.versa.flexvnf.versa_flexvnf import DEFAULT_PRIVILEGE_LEVELS


@pytest.mark.parametrize(
    "priv_pattern",
    [
        ("shell", "[admin@generic-hostname: ~] $ "),
        ("shell", "[admin@generic-hostname: tmp] $ "),
        ("cli", "admin@generic-hostname-cli> "),
        ("configuration", "admin@generic-hostname-cli(config)% "),
        ("configuration", "admin@generic-hostname-cli(config-interfaces)% "),
    ],
    ids=[
        "ssh_prompt_shell",
        "ssh_prompt_shell_folder",
        "ssh_prompt_cli",
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
