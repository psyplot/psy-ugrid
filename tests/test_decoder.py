# SPDX-FileCopyrightText: 2024 Helmholtz-Zentrum hereon GmbH
#
# SPDX-License-Identifier: LGPL-3.0-only

import psyplot.data as psyd

from psy_ugrid.decoder import UGridDecoder


def test_get_decoder(get_test_file):
    """Test to get the right decoder"""
    ds = psyd.open_dataset(get_test_file("simple_triangular_grid_si0.nc"))
    d = psyd.CFDecoder.get_decoder(ds, ds.Mesh2_fcvar)
    assert isinstance(d, UGridDecoder)
    return ds, d


def test_x(get_test_file):
    """Test the get_x method"""
    ds, d = test_get_decoder(get_test_file)
    x = d.get_x(ds.Mesh2_fcvar)
    assert "standard_name" in x.attrs
    assert x.attrs["standard_name"] == "longitude"
    rounded = list(map(lambda v: round(v, 3), x.values))
    assert rounded == [0.3, 0.567]


def test_y(get_test_file):
    """Test the get_y method"""
    ds, d = test_get_decoder(get_test_file)
    y = d.get_y(ds.Mesh2_fcvar)
    assert "standard_name" in y.attrs
    assert y.attrs["standard_name"] == "latitude"
    rounded = list(map(lambda v: round(v, 3), y.values))
    assert rounded == [0.4, 0.767]
