"""Submodule for the data structure and the reader of antenna logs."""


# standard library
from dataclasses import dataclass, field


# dependencies
from xarray_dataclasses import Attr, Data, Name


# submodules
from common import DEFAULT_FLOAT, T


# dataclasses
@dataclass
class Azimuth:
    """Representation of azimuth."""

    data: Data[T, float] = DEFAULT_FLOAT
    name: Name[str] = field(default="Azimuth", init=False)
    units: Attr[str] = field(default="degree", init=False)


@dataclass
class Elevation:
    """Representation of elevation."""

    data: Data[T, float] = DEFAULT_FLOAT
    name: Name[str] = field(default="Elevation", init=False)
    units: Attr[str] = field(default="degree", init=False)
