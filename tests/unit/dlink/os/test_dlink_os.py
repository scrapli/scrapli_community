import re

import pytest

from scrapli_community.dlink.os.dlink_os import DEFAULT_PRIVILEGE_LEVELS


@pytest.mark.parametrize(
    "priv_pattern",
    [
        ("exec", "Switch:admin#"),
        ("privilege_exec", "Switch:admin#"),
    ],
    ids=[
        "ssh_prompt_exec",
        "ssh_prompt_privilege_exec",
    ],
)
def test_default_prompt_patterns(priv_pattern):
    priv_level_name = priv_pattern[0]
    prompt = priv_pattern[1]
    prompt_pattern = DEFAULT_PRIVILEGE_LEVELS.get(priv_level_name).pattern
    match = re.search(pattern=prompt_pattern, string=prompt, flags=re.M | re.I)
    assert match
