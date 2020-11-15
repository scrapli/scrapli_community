import re

import pytest

from scrapli_community.aethra.atosnt.aethra_atosnt import SCRAPLI_PLATFORM


@pytest.mark.parametrize(
    "prompt",
    [
        "HOSTNAME>>",
        "SCRAPLI_AETHRA-ATOSNT_RTR>>",
        "SCRAPLI-1234>>",
    ],
)
def test_default_prompt_patterns(prompt):
    prompt_pattern = SCRAPLI_PLATFORM["defaults"]["comms_prompt_pattern"]
    match = re.search(pattern=prompt_pattern, string=prompt, flags=re.M | re.I)

    assert match
