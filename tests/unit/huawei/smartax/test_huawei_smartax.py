import re

import pytest

from scrapli_community.huawei.smartax.huawei_smartax import DEFAULT_PRIVILEGE_LEVELS


@pytest.mark.parametrize(
    "priv_pattern",
    [
        ("exec", "SCRAPLI-MA5800-X7>"),
        ("privilege_exec", "SCRAPLI_HUAWEI-SMARTAX_TEST_OLT1#"),
        ("configuration", "SCRAPLI_HUAWEI-SMARTAX_TEST_OLT1(config)#"),
        ("configuration", "SCRAPLI_HUAWEI-SMARTAX_TEST_OLT1(config-if-gpon-0/1)#"),
    ],
    ids=[
        "ssh_prompt_non_privileged_exec",
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
        ("configuration", "  VERSION : MA5800V100R018C10"),
        ("configuration", "  VERSION : MA5600V100R017C11"),
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
