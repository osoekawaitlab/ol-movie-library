from typing import Annotated, Literal

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
