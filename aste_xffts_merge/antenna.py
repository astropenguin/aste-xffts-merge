"""Submodule for the data structure and the reader of antenna logs."""


# standard library
from dataclasses import dataclass
from typing import Tuple


# dependencies
from xarray_dataclasses import AsDataset, Attr, Coordof, Data, Dataof, Name


# submodules
from common import DEFAULT_FLOAT, DEFAULT_TIME, readonly, Time, TimeAxis


# dataclasses
@dataclass
class Azimuth:
    """Representation of antenna azimuth."""

    data: Data[Time, float] = DEFAULT_FLOAT
    name: Name[str] = readonly("Azimuth")
    units: Attr[str] = readonly("degree")


@dataclass
class Elevation:
    """Representation of antenna elevation."""

    data: Data[Time, float] = DEFAULT_FLOAT
    name: Name[str] = readonly("Elevation")
    units: Attr[str] = readonly("degree")


@dataclass
class Longitude:
    """Representation of sky longitude."""

    data: Data[Time, float] = DEFAULT_FLOAT
    name: Name[str] = readonly("Longitude")
    units: Attr[str] = readonly("degree")


@dataclass
class Latitude:
    """Representation of sky latitude."""

    data: Data[Time, float] = DEFAULT_FLOAT
    name: Name[str] = readonly("Latitude")
    units: Attr[str] = readonly("degree")


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

    ref_longitude: Data[Tuple[()], float] = DEFAULT_FLOAT
    """Reference sky longitude (in degree)."""

    ref_latitude: Data[Tuple[()], float] = DEFAULT_FLOAT
    """Reference sky latitude (in degree)."""

    frame: Data[Tuple[()], str] = "ICRS"
    """Frame of sky coordinates."""

    t: Coordof[TimeAxis] = DEFAULT_TIME
    """Observed time (in UTC)."""
