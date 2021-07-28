import re

import pytest

from scrapli_community.paloalto.panos.paloalto_panos import DEFAULT_PRIVILEGE_LEVELS


@pytest.mark.parametrize(
    "priv_pattern",
    [
        ("exec", "admin@pdx-pa3020>"),
        ("exec", "admin.me@pdx-pa3020>"),
        ("exec", "admin.me.a@pdx-pa3020>"),
        ("configuration", "admin@pdx-pa3020#"),
        ("configuration", "admin.me@pdx-pa3020#"),
        ("configuration", "admin.me.a@pdx-pa3020#"),
    ],
    ids=[
        "base_prompt_exec",
        "base_prompt_exec_with_dot",
        "base_prompt_exec_with_2dots",
        "base_prompt_config",
        "base_prompt_config_with_dots",
        "base_prompt_config_with_2dots",
    ],
)
def test_default_prompt_patterns(priv_pattern):
    priv_level_name = priv_pattern[0]
    prompt = priv_pattern[1]
    prompt_pattern = DEFAULT_PRIVILEGE_LEVELS.get(priv_level_name).pattern
    match = re.search(pattern=prompt_pattern, string=prompt, flags=re.M | re.I)
    assert match
