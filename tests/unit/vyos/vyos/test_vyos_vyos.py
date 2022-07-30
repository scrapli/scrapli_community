import re

import pytest

from scrapli_community.vyos.vyos.vyos import DEFAULT_PRIVILEGE_LEVELS


@pytest.mark.parametrize(
    "priv_pattern",
    [
        ("privilege_exec", "vyos@Vy-31:~$"),
        ("privilege_exec", "vyos@Vy-31:/config/auth$"),
        ("configuration", "vyos@Vy-31#"),
    ],
)
def test_default_prompt_patterns(priv_pattern):
    priv_level_name = priv_pattern[0]
    prompt = priv_pattern[1]
    prompt_pattern = DEFAULT_PRIVILEGE_LEVELS.get(priv_level_name).pattern
    match = re.search(pattern=prompt_pattern, string=prompt, flags=re.M | re.I)
    assert match
