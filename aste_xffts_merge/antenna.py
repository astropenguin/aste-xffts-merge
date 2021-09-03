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
    """Representation of azimuth."""

    data: Data[Time, float] = DEFAULT_FLOAT
    name: Name[str] = readonly("Azimuth")
    units: Attr[str] = readonly("degree")


@dataclass
class Elevation:
    """Representation of elevation."""

    data: Data[Time, float] = DEFAULT_FLOAT
    name: Name[str] = readonly("Elevation")
    units: Attr[str] = readonly("degree")
