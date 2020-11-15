import re

import pytest

from scrapli_community.huawei.vrp.huawei_vrp import DEFAULT_PRIVILEGE_LEVELS


@pytest.mark.parametrize(
    "priv_pattern",
    [
        ("privilege_exec", "<SCRAPLI_HUAWEI-VRP_TEST_SW1>"),
        ("configuration", "[SCRAPLI_HUAWEI-VRP_TEST_SW1]"),
        ("configuration", "[SCRAPLI_HUAWEI-VRP_TEST_SW1-GigabitEthernet0/0/1]"),
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


@pytest.mark.parametrize(
    "priv_pattern",
    [
        ("configuration", "[V200R009C00SPC500]"),
        ("configuration", "[V300R009C10HP0006]"),
    ],
    ids=[
        "ssh_prompt_configuration",
        "ssh_prompt_configuration",
    ],
)
def test_prompt_patterns_ignore_version_string(priv_pattern):
    priv_level_name = priv_pattern[0]
    prompt = priv_pattern[1]

    prompt_pattern = DEFAULT_PRIVILEGE_LEVELS.get(priv_level_name).pattern
    match = re.search(pattern=prompt_pattern, string=prompt, flags=re.M | re.I)

    assert not match
