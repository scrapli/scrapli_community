import re
import textwrap

import pytest

from scrapli_community.fortinet.fortios.fortinet_fortios import SCRAPLI_PLATFORM


@pytest.mark.parametrize(
    "prompt",
    [
        "SCRAPLI-FORTIGATE # ",  # local admin root prompt
        "SCRAPLI-FORTIGATE $ ",  # remote admin root prompt
        "SCRAPLI-FORTIGATE (global) # ",  # global context
        "SCRAPLI-FORTIGATE (interface) # ",  # interface config context
        "SCRAPLI-FORTIGATE (ha-mgmt-interfaces) # ",  # subsection with dashes
        "SCRAPLI-FORTIGATE (vdom) # ",  # vdom config context
        "SCRAPLI-FORTIGATE (testvdom) # ",  # a user defined vdom context
    ],
)
def test_default_prompt_patterns(prompt):
    prompt_pattern = SCRAPLI_PLATFORM["defaults"]["comms_prompt_pattern"]
    match = re.search(pattern=prompt_pattern, string=prompt, flags=re.M | re.I)

    assert match


def test_default_prompt_not_matching_in_config():
    prompt_pattern = SCRAPLI_PLATFORM["defaults"]["comms_prompt_pattern"]
    text = textwrap.dedent(
        """\
    Let's assume this is a config text:
    somewhere I have a prompt like: HOSTNAME $ and some other text
    """
    )
    match = re.search(pattern=prompt_pattern, string=text, flags=re.M | re.I)

    assert not match
