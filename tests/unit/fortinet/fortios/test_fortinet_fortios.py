import re

import pytest

from scrapli_community.fortinet.fortios.fortinet_fortios import SCRAPLI_PLATFORM


@pytest.mark.parametrize(
    "prompt",
    [
        "SCRAPLI-FORTIGATE # ",  # local admin root prompt
        "SCRAPLI-FORTIGATE $ ",  # remote admin root prompt
        "SCRAPLI-FORTIGATE (global) # ",  # global context
        "SCRAPLI-FORTIGATE (interface) # ",  # interface config context
        "SCRAPLI-FORTIGATE (vdom) # ",  # vdom config context
        "SCRAPLI-FORTIGATE (testvdom) # ",  # a user defined vdom context
    ],
)
def test_default_prompt_patterns(prompt):
    prompt_pattern = SCRAPLI_PLATFORM["defaults"]["comms_prompt_pattern"]
    match = re.search(pattern=prompt_pattern, string=prompt, flags=re.M | re.I)

    assert match
