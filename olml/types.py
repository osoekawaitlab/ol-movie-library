from enum import Enum

import numpy as np
import numpy.typing as npt
from oltl import BaseBytes, Id, LowerBoundIntegerMixIn


class MovieId(Id):
    pass


class FrameId(Id):
    pass


class SegmentId(Id):
    pass


class SourceId(Id):
    pass


class MetadataId(Id):
    pass


class SourceType(str, Enum):
    LOCAL_FILE = "LOCAL_FILE"


class FrameNumber(LowerBoundIntegerMixIn):
    @classmethod
    def get_min_value(cls) -> int:
        return 0


class PictureBytes(BaseBytes):
    pass


class Image(npt.NDArray[np.uint8]): ...
