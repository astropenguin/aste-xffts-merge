"""Submodule of ASTE antenna logs."""


# standard library
from dataclasses import dataclass
from functools import partial
from pathlib import Path
from typing import Tuple, Union


# dependencies
import pandas as pd
import xarray as xr
import astropy.units as u
from astropy.coordinates import AltAz, EarthLocation, FK5, SkyCoord
from xarray_dataclasses import AsDataset, Attr, Coordof, Data, Dataof


# submodules
from .common import Time, const, time


# constants
ASTE_SITE = EarthLocation.from_geodetic(
    lon="-67d42m11.89525s",
    lat="-22d58m17.69447s",
    height="4861.9m",
)
LOG_COLUMNS = (
    "time",
    "ra_prog",
    "dec_prog",
    "az_prog",
    "el_prog",
    "az_real",
    "el_real",
    "az_error",
    "el_error",
)
LOG_FRAME = "RADEC"
LOG_SEPARATOR = r"\s+"
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
class Frame:
    """Sky coordinate frame."""

    data: Data[Tuple[()], str]
    long_name: Attr[str] = const("Sky coordinate frame")
    short_name: Attr[str] = const("Frame")


@dataclass
class Antenna(AsDataset):
    """ASTE antenna log."""

    time: Coordof[Time]
    """Time in UTC."""

    azimuth: Dataof[Azimuth]
    """Antenna azimuth (degree)."""

    elevation: Dataof[Elevation]
    """Antenna elevation (degree)."""

    longitude: Dataof[Longitude]
    """Sky longitude (degree)."""

    latitude: Dataof[Latitude]
    """Sky latitude (degree)."""

    frame: Attr[str]
    """Sky coordinate frame."""


# runtime functions
def read(path: Union[Path, str]) -> xr.Dataset:
    """Read an antenna log and create a Dataset object.

    Args:
        path: Path of the antenna log.

    Returns:
        A Dataset object that follows ``Antenna``.

    """
    # check if the sky coordinate frame is supported
    with open(path) as f:
        frame = f.readline().split()[0]

    if not frame == LOG_FRAME:
        raise ValueError(f"RADEC is only supported. Got {frame}.")

    # read the antenna log
    date_parser = partial(pd.to_datetime, format=LOG_TIMEFMT)

    log = pd.read_csv(
        path,
        date_parser=date_parser,
        index_col=0,
        names=LOG_COLUMNS,
        sep=LOG_SEPARATOR,
        skiprows=1,
    )

    # calculate real-prog differences in sky
    sky_prog = SkyCoord(
        alt=log[LOG_COLUMNS[4]],
        az=log[LOG_COLUMNS[3]],
        frame=AltAz,
        location=ASTE_SITE,
        obstime=log.index,
        unit=u.deg,  # type: ignore
    ).transform_to(FK5)

    sky_real = SkyCoord(
        alt=log[LOG_COLUMNS[6]],
        az=log[LOG_COLUMNS[5]],
        frame=AltAz,
        location=ASTE_SITE,
        obstime=log.index,
        unit=u.deg,  # type: ignore
    ).transform_to(FK5)

    d_lon = (sky_real.ra - sky_prog.ra).deg  # type: ignore
    d_lat = (sky_real.dec - sky_prog.dec).deg  # type: ignore

    return Antenna.new(
        time=log.index,
        azimuth=log[LOG_COLUMNS[5]],
        elevation=log[LOG_COLUMNS[6]],
        longitude=log[LOG_COLUMNS[1]] + d_lon,
        latitude=log[LOG_COLUMNS[2]] + d_lat,
        frame=FK5.name,  # type: ignore
    )
