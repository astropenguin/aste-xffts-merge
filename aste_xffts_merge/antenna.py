"""Submodule for the data structure and the reader of antenna logs."""


# standard library
from dataclasses import dataclass, field


# dependencies
from xarray_dataclasses import Attr, Data, Name


# submodules
from common import DEFAULT_FLOAT, Time


# dataclasses
@dataclass
class Azimuth:
    """Representation of azimuth."""

    data: Data[Time, float] = DEFAULT_FLOAT


@dataclass
class Elevation:
    """Representation of elevation."""

    data: Data[Time, float] = DEFAULT_FLOAT
