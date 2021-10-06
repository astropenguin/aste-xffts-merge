"""Submodule of ASTE antenna logs."""


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
from .common import Time, const, time


# constants
LOG_COLUMNS = "time", "longitude", "latitude", "azimuth", "elevation"
LOG_TIMEFMT = "%y%m%d%H%M%S.%f"


# dataclasses
@dataclass
class Azimuth:
    """Antenna azimuth (degree)."""

    data: Data[time, float]
    long_name: Attr[str] = const("Antenna azimuth")
    short_name: Attr[str] = const("Azimuth")
    units: Attr[str] = const("degree")


@dataclass
class Elevation:
    """Antenna elevation (degree)."""

    data: Data[time, float]
    long_name: Attr[str] = const("Antenna elevation")
    short_name: Attr[str] = const("Elevation")
    units: Attr[str] = const("degree")


@dataclass
class Longitude:
    """Sky longitude (degree)."""

    data: Data[time, float]
    long_name: Attr[str] = const("Sky longitude")
    short_name: Attr[str] = const("Longitude")
    units: Attr[str] = const("degree")


@dataclass
class Latitude:
    """Sky latitude (degree)."""

    data: Data[time, float]
    long_name: Attr[str] = const("Sky latitude")
    short_name: Attr[str] = const("Latitude")
    units: Attr[str] = const("degree")


@dataclass
class RefLongitude:
    """Reference sky longitude (degree)."""

    data: Data[Tuple[()], float]
    long_name: Attr[str] = const("Reference sky longitude")
    short_name: Attr[str] = const("Ref. longitude")
    units: Attr[str] = const("degree")


@dataclass
class RefLatitude:
    """Reference sky latitude (degree)."""

    data: Data[Tuple[()], float]
    long_name: Attr[str] = const("Reference sky latitude")
    short_name: Attr[str] = const("Ref. latitude")
    units: Attr[str] = const("degree")


@dataclass
class Frame:
    """Sky coordinate frame."""

    data: Data[Tuple[()], str]
    long_name: Attr[str] = const("Sky coordinate frame")
    short_name: Attr[str] = const("Frame")


@dataclass
class Antenna(AsDataset):
    """ASTE antenna log."""

    azimuth: Dataof[Azimuth] = 0.0
    """Antenna azimuth (degree)."""

    elevation: Dataof[Elevation] = 0.0
    """Antenna elevation (degree)."""

    longitude: Dataof[Longitude] = 0.0
    """Sky latitude (degree)."""

    latitude: Dataof[Latitude] = 0.0
    """Sky latitude (degree)."""

    ref_longitude: Dataof[RefLongitude] = 0.0
    """Reference sky longitude (degree)."""

    ref_latitude: Dataof[RefLatitude] = 0.0
    """Reference sky latitude (degree)."""

    frame: Dataof[Frame] = "RADEC"
    """Sky coordinate frame."""

    time: Coordof[Time] = "2000-01-01"
    """Time in UTC."""


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
        time=data.index,
    )
