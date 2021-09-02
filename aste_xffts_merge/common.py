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
T = Literal["t"]
Ch = Literal["ch"]
Time = Literal["datetime64[ns]"]


# dataclasses
@dataclass
class TAxis:
    """Representation of the time axis (in UTC)."""

    data: Data[T, Time] = DEFAULT_TIME
    name: Name[str] = field(default="Time", init=False)


@dataclass
class ChAxis:
    """Representation of the channel axis."""

    data: Data[Ch, int] = DEFAULT_INT
    name: Name[str] = field(default="Channel", init=False)
