"""Submodule for the data structure and the reader of antenna logs."""


# standard library
from dataclasses import dataclass


# dependencies
from xarray_dataclasses import Attr, Data, Name


# submodules
from common import DEFAULT_FLOAT, readonly, Time


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
