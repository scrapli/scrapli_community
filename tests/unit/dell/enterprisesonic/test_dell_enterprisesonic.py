import re

import pytest

from scrapli_community.dell.enterprisesonic.sonic import DEFAULT_PRIVILEGE_LEVELS


@pytest.mark.parametrize(
    "priv_pattern",
    [
        ("linux", "user@scrapli-test-SONiC:~$ "),
        ("linux", "root@scrapli-test-SONiC:/home/user# "),
        ("exec", "scrapli-test-SONiC# "),
        ("configuration", "scrapli-test-SONiC(config)# "),
        ("configuration", "scrapli-test-SONiC(config-subif-Eth1/56.666)# "),
    ],
    ids=[
        "linux",
        "linux_root",
        "exec",
        "configuration",
        "configuration_subif",
    ],
)
def test_default_prompt_patterns(priv_pattern):
    priv_level_name = priv_pattern[0]
    prompt = priv_pattern[1]

    prompt_pattern = DEFAULT_PRIVILEGE_LEVELS.get(priv_level_name).pattern
    match = re.search(pattern=prompt_pattern, string=prompt, flags=re.M | re.I)

    assert match
