from enum import Enum

from oltl import BaseBytes, Id, LowerBoundFloatMixIn, LowerBoundIntegerMixIn


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


class FrameTime(LowerBoundFloatMixIn):
    @classmethod
    def get_min_value(cls) -> float:
        return 0.0


class PictureBytes(BaseBytes):
    pass
