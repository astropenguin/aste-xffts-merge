# standard library
from pathlib import Path


# dependencies
import numpy as np


# submodules
from aste_xffts_merge.antenna import read


# constants
DATA_DIR = Path("data")


# test data
antenna = read(DATA_DIR / "antlog_20160925054612")
azimuth = antenna.azimuth
elevation = antenna.elevation
longitude = antenna.longitude
latitude = antenna.latitude
frame = antenna.attrs["frame"]
time = antenna.time


# test functions
def test_azimuth() -> None:
    assert azimuth.data[0] == 32.33328
    assert azimuth.data[-1] == 27.23588
    assert azimuth.dims == ("time",)
    assert azimuth.dtype == float
    assert azimuth.long_name == "Antenna azimuth"
    assert azimuth.short_name == "Azimuth"
    assert azimuth.units == "degree"


def test_elevation() -> None:
    assert elevation.data[0] == 66.70913
    assert elevation.data[-1] == 67.71098
    assert elevation.dims == ("time",)
    assert elevation.dtype == float
    assert elevation.long_name == "Antenna elevation"
    assert elevation.short_name == "Elevation"
    assert elevation.units == "degree"


def test_longitude() -> None:
    assert longitude.data[0] == 35.22711008825143
    assert longitude.data[-1] == 34.920058122516124
    assert longitude.dims == ("time",)
    assert longitude.dtype == float
    assert longitude.long_name == "Sky longitude"
    assert longitude.short_name == "Longitude"
    assert longitude.units == "degree"


def test_latitude() -> None:
    assert latitude.data[0] == -2.9800510859615605
    assert latitude.data[-1] == -2.978326544768754
    assert latitude.dims == ("time",)
    assert latitude.dtype == float
    assert latitude.long_name == "Sky latitude"
    assert latitude.short_name == "Latitude"
    assert latitude.units == "degree"


def test_frame() -> None:
    assert frame == "fk5"


def test_t() -> None:
    assert time.data[0] == np.datetime64("2016-09-25T05:46:14.600000000")
    assert time.data[-1] == np.datetime64("2016-09-25T05:53:50.500000000")
    assert time.dims == ("time",)
    assert time.dtype.type == np.datetime64
    assert time.long_name == "Time in UTC"
    assert time.short_name == "Time"
