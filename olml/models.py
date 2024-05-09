from typing import Annotated, Literal, cast

import cv2
import numpy as np
import numpy.typing as npt
from oltl import BaseEntity, BaseUpdateTimeAwareModel
from pydantic import Field, FilePath

from .types import (
    FrameId,
    FrameNumber,
    MetadataId,
    MovieId,
    PictureBytes,
    SegmentId,
    SourceId,
    SourceType,
)


class Metadata(BaseEntity[MetadataId], BaseUpdateTimeAwareModel):  # type: ignore[misc]
    pass


class BaseMovieSource(BaseEntity[SourceId], BaseUpdateTimeAwareModel):  # type: ignore[misc]
    type: SourceType


class LocalFileSource(BaseMovieSource):
    type: Literal[SourceType.LOCAL_FILE] = SourceType.LOCAL_FILE
    path: FilePath


Source = Annotated[LocalFileSource, Field(discriminator="type")]


class Movie(BaseEntity[MovieId], BaseUpdateTimeAwareModel):  # type: ignore[misc]
    source: Source


class Segment(BaseEntity[SegmentId], BaseUpdateTimeAwareModel):  # type: ignore[misc]
    movie: MovieId
    start_frame: FrameId
    end_frame: FrameId


class Frame(BaseEntity[FrameId], BaseUpdateTimeAwareModel):  # type: ignore[misc]
    number: FrameNumber
    picture_bytes: PictureBytes
    segment: SegmentId

    @property
    def image(self) -> npt.NDArray[np.uint8]:
        self._image: npt.NDArray[np.uint8]
        if not hasattr(self, "_image") or self._image is None:
            self._image = cast(
                npt.NDArray[np.uint8], cv2.imdecode(np.frombuffer(self.picture_bytes, dtype=np.uint8), cv2.IMREAD_COLOR)
            )
        return self._image
