import re

import pytest

from scrapli_community.lantronix.itmgos.lantronix_itmgos import DEFAULT_PRIVILEGE_LEVELS


@pytest.mark.parametrize(
    "priv_pattern",
    [
        ("exec", "[SLC9032]>"),
        ("exec", "[SLC9016-16U-16E]> "),
        ("exec", "[slc8032-lab]>"),
        ("exec", "[EMG8500.example]>"),
        ("exec", "[edge_console_01]> "),
    ],
    ids=["slc9000", "slc9000_sku", "slc8000_hyphen", "emg_dotted", "underscore"],
)
def test_default_prompt_patterns(priv_pattern):
    priv_level_name = priv_pattern[0]
    prompt = priv_pattern[1]

    prompt_pattern = DEFAULT_PRIVILEGE_LEVELS.get(priv_level_name).pattern
    match = re.search(pattern=prompt_pattern, string=prompt, flags=re.M | re.I)

    assert match


@pytest.mark.parametrize(
    "prompt",
    ["SLC9032>", "[SLC9032]#", "Do you want to continue? [no] ", "login: "],
    ids=["no_brackets", "hash", "confirm_question", "login"],
)
def test_default_prompt_patterns_reject(prompt):
    prompt_pattern = DEFAULT_PRIVILEGE_LEVELS.get("exec").pattern
    assert not re.search(pattern=prompt_pattern, string=prompt, flags=re.M | re.I)
