# dependencies
import numpy as np
import pandas as pd
from xarray_dataclasses import asdataarray


# submodules
from aste_xffts_merge.common import Time, Chan


# test data
time = asdataarray(Time(pd.date_range("2000-01-01", periods=5)))
chan = asdataarray(Chan(np.arange(5)))


# test functions
def test_time_axis() -> None:
    assert time.dims == ("time",)
    assert time.dtype == np.dtype("M8[ns]")
    assert time.long_name == "Time in UTC"
    assert time.short_name == "Time"


def test_chan_axis() -> None:
    assert chan.dims == ("chan",)
    assert chan.dtype == np.dtype("int64")
    assert chan.long_name == "Channel ID"
    assert chan.short_name == "Channel"
