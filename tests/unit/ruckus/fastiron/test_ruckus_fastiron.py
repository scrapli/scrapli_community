import re

import pytest

from scrapli_community.ruckus.fastiron.ruckus_fastiron import DEFAULT_PRIVILEGE_LEVELS


@pytest.mark.parametrize(
    "priv_pattern",
    [
        ("exec", "ICX7150-24-Switch>"),
        ("privilege_exec", "ICX7150-24-Switch#"),
        ("configuration", "ICX7150-24-Switch(config)#"),
        ("configuration", "ICX7150-24-Switch(config-if-e1000-1/1/1)#"),
        ("exec", "SSH@ICX7150-24-Switch>"),
        ("privilege_exec", "SSH@ICX7150-24-Switch#"),
        ("configuration", "SSH@ICX7150-24-Switch(config)#"),
        ("configuration", "SSH@ICX7150-24-Switch(config-if-e1000-1/1/1)#"),
    ],
    ids=[
        "base_prompt_exec",
        "base_prompt_privilege_exec",
        "base_prompt_configuration",
        "base_prompt_configuration_interface",
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
