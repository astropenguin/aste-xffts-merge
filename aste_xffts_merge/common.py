"""Submodule that defines objects commonly used within the package."""


# standard library
from dataclasses import dataclass, field
from typing import Literal


# dependencies
from xarray_dataclasses import Data, Name


# constants
DEFAULT_FLOAT = 0.0
DEFAULT_INT = 0
DEFAULT_STR = ""
DEFAULT_TIME = "2000-01-01"
DIMS = "t", "ch"


# type hints
Time = Literal["t"]
Chan = Literal["ch"]
DT64 = Literal["datetime64[ns]"]


# dataclasses
@dataclass
class TimeAxis:
    """Representation of the time axis (in UTC)."""

    data: Data[Time, DT64] = DEFAULT_TIME


@dataclass
class ChanAxis:
    """Representation of the channel axis."""

    data: Data[Chan, int] = DEFAULT_INT
