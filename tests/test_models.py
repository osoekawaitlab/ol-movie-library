import os

from olml.models import Frame
from olml.types import SegmentId


def test_frame_image() -> None:
    wd = os.path.dirname(os.path.abspath(__file__))
    fixture_dir = os.path.join(wd, "fixtures")
    with open(os.path.join(fixture_dir, "192x108noise.png"), "rb") as f:
        frame = Frame(number=1, picture_bytes=f.read(), segment=SegmentId("01HXEP0PWMYE77Z1M8FPPYPTHJ"), time=0.0)
    assert frame.image.shape == (108, 192, 3)
    assert frame.image.dtype == "uint8"
    assert frame.image[0, 0, 0] == 89
    assert frame.image[0, 0, 1] == 89
    assert frame.image[0, 0, 2] == 153
