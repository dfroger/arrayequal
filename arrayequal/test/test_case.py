#!/usr/bin/env python
import unittest

import  numpy as np

import sys
sys.path.append('..')
from case import NumTestCase
from comparer import ArrayComparer

ZERO,ONE = 0., 1.
PICO,TERA = 1E-12, 1E+12
RTOL = 1.E-15

class LyingArrayComparer(ArrayComparer):

    def are_equal(self,val1,val2): 
        return True

class TestNumTestCase(NumTestCase):

    def test_assert_equal(self):
        a1 = np.array( [1,2,3,] )
        a2 = np.array( [1,2,3,] )
        self.assertEqual(a1, a2)

    def test_assert_not_equal(self):
        a1 = np.array( [1,2,3,4] )
        a2 = np.array( [1,2,3,] )
        self.assertNotEqual(a1, a2)

    def test_assert_array_equal(self):
        a1 = np.array( [1,2,3,] )
        a2 = np.array( [1,2,3,] )
        self.assertArrayEqual(a1, a2)

    def test_assert_array_almost_equal(self):
        a1 = np.array( [TERA,]*3 )
        a2 = np.array( [TERA+PICO,]*3 )
        self.assertArrayAlmostEqual(a1,a2)

    def test_assert_array_almost_custom_comparer(self):
        a1 = np.array( [1,2,3] )
        a2 = np.array( [10,20,30] )
        self.assertArrayAlmostEqual(a1,a2,comparer=LyingArrayComparer())

if __name__ == '__main__':
    unittest.main()
