from __future__ import absolute_import

import pyfits
import sunpy
from sunpy.wcs import wcs as wcs
from numpy.testing import assert_array_almost_equal

fits = pyfits.open(sunpy.AIA_171_IMAGE)
header = fits[0].header

def test_conv_hpc_hcc():
    coord = [40.0, 32.0]
    result = wcs.convert_hpc_hcc(header, coord[0], coord[1])
    assert_array_almost_equal(result, [28748691, 22998953], decimal=3)
 
def test_conv_hcc_hpc():
    coord = [34.0, 132.0]
    result = wcs.convert_hcc_hpc(header, coord[0], coord[1])
    assert_array_almost_equal(result, [1.3140782e-08, 5.1017152e-08], decimal=2)

def test_conv_hcc_hg():
    coord = [13.0, 58.0]
    result = wcs.convert_hcc_hg(header, coord[0], coord[1])
    assert_array_almost_equal(result, [1.0791282e-06, -7.0640732], decimal=2)

def test_conv_hg_hcc():
    coord = [34.0, 96.0]
    result = wcs.convert_hg_hcc(header, coord[0], coord[1])
    assert_array_almost_equal(result, [-40653538.0, 6.7903529e08], decimal=2)
    
def test_conv_hg_hpc():
    coord = [34.0, 96.0]
    result = wcs.convert_hg_hpc(header, coord[0], coord[1])
    assert_array_almost_equal(result, [0.096365756, 0.22138465], decimal=2)
    
