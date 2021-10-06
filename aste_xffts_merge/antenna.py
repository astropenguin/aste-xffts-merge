"""Submodule for the data structure and the reader of antenna logs."""


# standard library
from dataclasses import dataclass
from functools import partial
from pathlib import Path
from typing import Tuple, Union


# dependencies
import pandas as pd
import xarray as xr
from xarray_dataclasses import AsDataset, Attr, Coordof, Data, Dataof


# submodules
from .common import (
    DEFAULT_FLOAT,
    DEFAULT_FRAME,
    DEFAULT_TIME,
    Time,
    TimeAxis,
    const,
)


# constants
LOG_COLUMNS = "time", "longitude", "latitude", "azimuth", "elevation"
LOG_TIMEFMT = "%y%m%d%H%M%S.%f"


# dataclasses
@dataclass
class Azimuth:
    """Representation of antenna azimuth."""

    data: Data[Time, float] = DEFAULT_FLOAT
    long_name: Attr[str] = const("Antenna azimuth")
    standard_name: Attr[str] = const("Azimuth")
    units: Attr[str] = const("degree")


@dataclass
class Elevation:
    """Representation of antenna elevation."""

    data: Data[Time, float] = DEFAULT_FLOAT
    long_name: Attr[str] = const("Antenna elevation")
    standard_name: Attr[str] = const("Elevation")
    units: Attr[str] = const("degree")


@dataclass
class Longitude:
    """Representation of sky longitude."""

    data: Data[Time, float] = DEFAULT_FLOAT
    long_name: Attr[str] = const("Sky longitude")
    standard_name: Attr[str] = const("Longitude")
    units: Attr[str] = const("degree")


@dataclass
class Latitude:
    """Representation of sky latitude."""

    data: Data[Time, float] = DEFAULT_FLOAT
    long_name: Attr[str] = const("Sky latitude")
    standard_name: Attr[str] = const("Latitude")
    units: Attr[str] = const("degree")


@dataclass
class RefLongitude:
    """Representation of reference sky longitude."""

    data: Data[Tuple[()], float] = DEFAULT_FLOAT
    long_name: Attr[str] = const("Reference sky longitude")
    standard_name: Attr[str] = const("Ref. longitude")
    units: Attr[str] = const("degree")


@dataclass
class RefLatitude:
    """Representation of reference sky latitude."""

    data: Data[Tuple[()], float] = DEFAULT_FLOAT
    long_name: Attr[str] = const("Reference sky latitude")
    standard_name: Attr[str] = const("Ref. latitude")
    units: Attr[str] = const("degree")


@dataclass
class Frame:
    """Representation of sky coordinate frame."""

    data: Data[Tuple[()], str] = DEFAULT_FRAME
    long_name: Attr[str] = const("Sky coordinate frame")
    standard_name: Attr[str] = const("Frame")


@dataclass
class Antenna(AsDataset):
    """Representation of antenna log."""

    azimuth: Dataof[Azimuth] = DEFAULT_FLOAT
    """Antenna azimuth (in degree)."""

    elevation: Dataof[Elevation] = DEFAULT_FLOAT
    """Antenna elevation (in degree)."""

    longitude: Dataof[Longitude] = DEFAULT_FLOAT
    """Sky latitude (in degree)."""

    latitude: Dataof[Latitude] = DEFAULT_FLOAT
    """Sky latitude (in degree)."""

    ref_longitude: Dataof[RefLongitude] = DEFAULT_FLOAT
    """Reference sky longitude (in degree)."""

    ref_latitude: Dataof[RefLatitude] = DEFAULT_FLOAT
    """Reference sky latitude (in degree)."""

    frame: Dataof[Frame] = DEFAULT_FRAME
    """Sky coordinate frame."""

    t: Coordof[TimeAxis] = DEFAULT_TIME
    """Observed time (in UTC)."""


# runtime functions
def read(path: Union[Path, str]) -> xr.Dataset:
    """Read an antenna log and create a Dataset object.

    Args:
        path: Path of the antenna log.

    Returns:
        A Dataset object that follows ``Antenna``.

    """
    # read header part
    with open(path) as f:
        header = f.readline().split()

    frame, _, ref_longitude, ref_latitude = header

    # read data part
    date_parser = partial(pd.to_datetime, format=LOG_TIMEFMT)

    data = pd.read_csv(
        path,
        date_parser=date_parser,
        index_col=0,
        names=LOG_COLUMNS,
        sep=r"\s+",
        skiprows=1,
        usecols=range(len(LOG_COLUMNS)),
    )

    return Antenna.new(
        azimuth=data.azimuth,
        elevation=data.elevation,
        longitude=data.longitude,
        latitude=data.latitude,
        ref_longitude=ref_longitude,
        ref_latitude=ref_latitude,
        frame=frame,
        t=data.index,
    )
