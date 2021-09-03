# dependencies
import numpy as np
import pandas as pd
from xarray_dataclasses import asdataarray


# submodules
from aste_xffts_merge.common import TimeAxis, ChanAxis


# test data
t = asdataarray(TimeAxis(pd.date_range("2000-01-01", periods=5)))
ch = asdataarray(ChanAxis(np.arange(5)))


# test functions
def test_time_axis() -> None:
    assert t.dims == ("t",)
    assert t.dtype == np.dtype("datetime64[ns]")
    assert t.long_name == "Observed time"
    assert t.standard_name == "Time"


def test_chan_axis() -> None:
    assert ch.dims == ("ch",)
    assert ch.dtype == np.dtype("int64")
    assert ch.long_name == "Channel ID"
    assert ch.standard_name == "Channel"
