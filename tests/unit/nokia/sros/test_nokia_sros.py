import re

import pytest

from scrapli_community.nokia.sros.nokia_sros import (
    CLASSIC_DEFAULT_PRIVILEGE_LEVELS,
    DEFAULT_PRIVILEGE_LEVELS,
)


@pytest.mark.parametrize(
    "priv_pattern",
    [
        ("exec", "[/]\nA:admin@sr1#"),
        ("configuration", "(ex)[/]\nA:admin@sr1#"),
        ("configuration", "*(ex)[/]\nA:admin@sr1#"),
        ("configuration", "!(ex)[/]\nA:admin@sr1#"),
        ("configuration", "(ex)[]\nA:admin@sr1#"),
        ("configuration_with_path", "(ex)[/somepath]\nA:admin@sr1#"),
        ("configuration_with_path", "*(ex)[/somepath]\nA:admin@sr1#"),
        ("configuration_with_path", "!(ex)[/somepath]\nA:admin@sr1#"),
    ],
    ids=[
        "exec",
        "configuration",
        "configuration_pending_change",
        "configuration_datastore_change",
        "configuration_no_path",
        "configuration_with_path",
        "configuration_with_path_pending_change",
        "configuration_with_path_datastore_change",
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
        ("exec", "*A:sr1#"),
        ("exec", "*B:DEV02-XY2#"),
        ("configuration", "*A:sr1>config#"),
        ("exec", "*A:ear1.sr7s-1# "),
        ("configuration", "*A:ear1.sr7s-1>config>port# "),
    ],
    ids=[
        "exec",
        "exec-hyphen",
        "configuration",
        "exec-period",
        "configuration-period",
    ],
)
def test_default_prompt_patterns_classic_variant(priv_pattern):
    priv_level_name = priv_pattern[0]
    prompt = priv_pattern[1]

    prompt_pattern = CLASSIC_DEFAULT_PRIVILEGE_LEVELS.get(priv_level_name).pattern
    match = re.search(pattern=prompt_pattern, string=prompt, flags=re.M | re.I)

    assert match
