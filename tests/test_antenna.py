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
ref_longitude = antenna.ref_longitude
ref_latitude = antenna.ref_latitude
frame = antenna.frame
time = antenna.time


# test functions
def test_azimuth() -> None:
    assert azimuth.data[0] == 31.65207
    assert azimuth.data[-1] == 27.23589
    assert azimuth.dims == ("time",)
    assert azimuth.dtype == float
    assert azimuth.long_name == "Antenna azimuth"
    assert azimuth.short_name == "Azimuth"
    assert azimuth.units == "degree"


def test_elevation() -> None:
    assert elevation.data[0] == 66.85711
    assert elevation.data[-1] == 67.71096
    assert elevation.dims == ("time",)
    assert elevation.dtype == float
    assert elevation.long_name == "Antenna elevation"
    assert elevation.short_name == "Elevation"
    assert elevation.units == "degree"


def test_longitude() -> None:
    assert longitude.data[0] == 34.92007
    assert longitude.data[-1] == 34.92007
    assert longitude.dims == ("time",)
    assert longitude.dtype == float
    assert longitude.long_name == "Sky longitude"
    assert longitude.short_name == "Longitude"
    assert longitude.units == "degree"


def test_latitude() -> None:
    assert latitude.data[0] == -2.97831
    assert latitude.data[-1] == -2.97831
    assert latitude.dims == ("time",)
    assert latitude.dtype == float
    assert latitude.long_name == "Sky latitude"
    assert latitude.short_name == "Latitude"
    assert latitude.units == "degree"


def test_ref_longitude() -> None:
    assert ref_longitude.data.item() == 34.83662
    assert ref_longitude.dims == ()
    assert ref_longitude.dtype == float
    assert ref_longitude.long_name == "Reference sky longitude"
    assert ref_longitude.short_name == "Ref. longitude"
    assert ref_longitude.units == "degree"


def test_ref_latitude() -> None:
    assert ref_latitude.data.item() == -2.97831
    assert ref_latitude.dims == ()
    assert ref_latitude.dtype == float
    assert ref_latitude.long_name == "Reference sky latitude"
    assert ref_latitude.short_name == "Ref. latitude"
    assert ref_latitude.units == "degree"


def test_frame() -> None:
    assert frame.data.item() == "RADEC"
    assert frame.dims == ()
    assert frame.dtype.type == np.str_
    assert frame.long_name == "Sky coordinate frame"
    assert frame.short_name == "Frame"


def test_t() -> None:
    assert time.data[0] == np.datetime64("2016-09-25T05:46:14.600000000")
    assert time.data[-1] == np.datetime64("2016-09-25T05:53:50.500000000")
    assert time.dims == ("time",)
    assert time.dtype.type == np.datetime64
    assert time.long_name == "Time in UTC"
    assert time.short_name == "Time"
