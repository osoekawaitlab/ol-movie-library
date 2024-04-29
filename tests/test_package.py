import re

import olml


def test_version() -> None:
    assert re.match(r"\d+\.\d+\.\d+", olml.__version__)
