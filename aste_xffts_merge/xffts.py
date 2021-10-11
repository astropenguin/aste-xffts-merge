"""Submodule of the ASTE XFFTS logs."""


# standard library
from dataclasses import dataclass
from functools import partial
from pathlib import Path
from typing import Literal, Tuple, Union


# dependencies
import numpy as np
import pandas as pd
import xarray as xr
from xarray_dataclasses import AsDataset, Attr, Coordof, Data, Dataof


# submodules
from .common import Chan, Time, chan, const, time


# constants
LOG_NCHAN = 32768
LOG_COLUMNS = "time", "integtime", "obsmode", "spectrum"
LOG_DTYPES = "f8", "f4", "S8", ("f4", LOG_NCHAN)
LOG_TIMEFMT = dict(unit="s")


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
def read(path: Union[Path, str]) -> xr.Dataset:
    """Read an XFFTS log and create a Dataset object.

    Args:
        path: Path of the XFFTS log.

    Returns:
        A Dataset object created by ``XFFTS``.

    """
    dtype = list(zip(LOG_COLUMNS, LOG_DTYPES))
    to_datetime = partial(pd.to_datetime, **LOG_TIMEFMT)

    with open(path, "rb") as f:
        log = np.frombuffer(f.read(), dtype=dtype)

    return XFFTS.new(
        time=to_datetime(log[LOG_COLUMNS[0]]),
        chan=np.arange(LOG_NCHAN),
        integtime=log[LOG_COLUMNS[1]],
        obsmode=log[LOG_COLUMNS[2]],
        spectrum=log[LOG_COLUMNS[3]],
    )
