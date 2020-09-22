import re

import pytest

from scrapli_community.mikrotik.routeros.mikrotik_routeros import SCRAPLI_PLATFORM


@pytest.mark.parametrize(
    "prompt",
    [
        "[username@HOSTNAME] > ",
        "[username@SCRAPLI_MIKROTIK-ROS_TEST_RTR] > ",
        "[username@SCRAPLI1234] > ",
        "[username@SCRAPLI-TEST-ROUTER] > ",
        "[username@SCRAPLI-TEST-ROUTER] /interface> ",
        "[username@SCRAPLI-TEST-ROUTER] /system console> ",
    ],
)
def test_default_prompt_patterns(prompt):
    prompt_pattern = SCRAPLI_PLATFORM["defaults"]["comms_prompt_pattern"]
    match = re.search(pattern=prompt_pattern, string=prompt, flags=re.M | re.I)

    assert match
