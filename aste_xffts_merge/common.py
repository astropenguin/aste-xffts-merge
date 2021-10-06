"""Submodule of common objects within the package."""


# standard library
from dataclasses import dataclass, field
from typing import Any, Literal, TypeVar


# dependencies
from xarray_dataclasses import Attr, Data


# constants
DIMS = "time", "chan"


# type hints
T = TypeVar("T")
time = Literal["time"]
chan = Literal["chan"]


# dataclasses
def const(default: T, **kwargs: Any) -> T:
    """Create a constant field for dataclasses."""
    return field(default=default, init=False, **kwargs)


@dataclass
class Time:
    """Time in UTC."""

    data: Data[time, Literal["M8[ns]"]]
    long_name: Attr[str] = const("Time in UTC")
    short_name: Attr[str] = const("Time")


@dataclass
class Chan:
    """Channel ID."""

    data: Data[chan, int]
    long_name: Attr[str] = const("Channel ID")
    short_name: Attr[str] = const("Channel")
