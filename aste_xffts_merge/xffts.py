"""Submodule of the ASTE XFFTS logs."""


# standard library
from dataclasses import dataclass
from typing import Literal, Tuple


# dependencies
from xarray_dataclasses import AsDataset, Attr, Coordof, Data, Dataof


# submodules
from .common import Chan, Time, chan, const, time


# constants


# dataclasses
@dataclass
class IntegTime:
    """Integration time per sample."""

    data: Data[time, Literal["f4"]]
    long_name: Attr[str] = const("Integration time")
    short_name: Attr[str] = const("Integ. time")
    units: Attr[str] = const("s")


@dataclass
class ObsMode:
    """Observation mode per sample."""

    data: Data[time, Literal["U8"]]
    long_name: Attr[str] = const("Observation mode")
    short_name: Attr[str] = const("Obs. mode")


@dataclass
class Spectrum:
    """Sampled XFFTS spectrum."""

    data: Data[Tuple[time, chan], Literal["f4"]]
    long_name: Attr[str] = const("XFFTS spectrum")
    short_name: Attr[str] = const("Spectrum")


@dataclass
class XFFTS(AsDataset):
    """XFFTS logging data."""

    time: Coordof[Time]
    """Observed time (in UTC)."""

    chan: Coordof[Chan]
    """Channel number."""

    integtime: Dataof[IntegTime]
    """Integration time per sample."""

    obsmode: Dataof[ObsMode]
    """Observation mode per sample."""

    spectrum: Dataof[Spectrum]
    """Sampled XFFTS spectrum."""


# runtime functions
