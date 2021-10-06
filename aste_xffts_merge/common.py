"""Submodule that defines objects commonly used within the package."""


# standard library
from dataclasses import dataclass, field
from typing import Any, Literal, TypeVar


# dependencies
from xarray_dataclasses import Attr, Data


# constants
DEFAULT_FLOAT = 0.0
DEFAULT_FRAME = "RADEC"
DEFAULT_INT = 0
DEFAULT_STR = ""
DEFAULT_TIME = "2000-01-01"
DIMS = "t", "ch"


# type hints
T = TypeVar("T")
Time = Literal["t"]
Chan = Literal["ch"]
DT64 = Literal["datetime64[ns]"]


# dataclasses
def const(default: T, **kwargs: Any) -> T:
    """Create a constant field for dataclasses."""
    return field(default=default, init=False, **kwargs)


@dataclass
class TimeAxis:
    """Representation of the time axis (in UTC)."""

    data: Data[Time, DT64] = DEFAULT_TIME
    long_name: Attr[str] = const("Observed time")
    standard_name: Attr[str] = const("Time")


@dataclass
class ChanAxis:
    """Representation of the channel axis."""

    data: Data[Chan, int] = DEFAULT_INT
    long_name: Attr[str] = const("Channel ID")
    standard_name: Attr[str] = const("Channel")
