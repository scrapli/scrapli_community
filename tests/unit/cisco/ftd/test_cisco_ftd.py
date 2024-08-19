import re

import pytest

from scrapli_community.cisco.ftd.cisco_ftd import DEFAULT_PRIVILEGE_LEVELS


@pytest.mark.parametrize(
    "priv_pattern",
    [
        ("exec", ">"),
        ("exec", "> "),
        ("expert", "my-user@ACME-FIREWALL:~$"),
        ("expert", "my-user@ACME-FIREWALL:~$ "),
        ("root", "root@ACME-FIREWALL:~#"),
        ("root", "root@ACME-FIREWALL:~# "),
    ],
    ids=[
        "base_prompt_exec",
        "base_prompt_exec_space",
        "base_prompt_expert",
        "base_prompt_expert_space",
        "base_prompt_root",
        "base_prompt_root_space",
    ],
)
def test_default_prompt_patterns(priv_pattern):
    priv_level_name = priv_pattern[0]
    prompt = priv_pattern[1]
    prompt_pattern = DEFAULT_PRIVILEGE_LEVELS.get(priv_level_name).pattern
    match = re.search(pattern=prompt_pattern, string=prompt, flags=re.M | re.I)
    assert match
