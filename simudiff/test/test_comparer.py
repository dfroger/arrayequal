#!/usr/bin/env python
import unittest

import numpy as np

from simudiff.comparer import SymetricArrayComparer, ExactArrayComparer

ZERO,ONE = 0., 1.
PICO,TERA = 1E-12, 1E+12
RTOL = 1.E-15

class TestExact(unittest.TestCase):

    def test_scalars(self):
        comparer = ExactArrayComparer()
        self.assertTrue(comparer.are_equal(ZERO,ZERO))
        self.assertFalse(comparer.are_equal(ONE,ZERO))
        self.assertFalse(comparer.are_equal(ZERO,ONE))
        self.assertFalse(comparer.are_equal(PICO+ONE,PICO))
        self.assertFalse(comparer.are_equal(PICO,PICO+ONE))
        self.assertTrue(comparer.are_equal(TERA,TERA+PICO))
        self.assertTrue(comparer.are_equal(TERA+PICO,TERA))

    def test_equal(self):
        a1 = np.array([1,2,3])
        a2 = np.array([1,2,3])
        comparer = ExactArrayComparer()
        comparer(a1,a2)

    def test_different_shape(self):
        a1 = np.array([1,2,3])
        a2 = np.array([1,2,3.1])
        comparer = ExactArrayComparer()
        with self.assertRaises(AssertionError):
            comparer(a1,a2)

    def test_different_data_type(self):
        a1 = np.array([1,2,3], dtype='int32')
        a2 = np.array([1,2,3], dtype='int64')
        comparer = ExactArrayComparer()
        with self.assertRaises(AssertionError):
            comparer(a1,a2)

    def test_arg1_not_numpy_array(self):
        a1 = [1,2,3]
        a2 = np.array([1,2,3])
        comparer = ExactArrayComparer()
        with self.assertRaises(AssertionError):
            comparer(a1,a2)

    def test_arg2_not_numpy_array(self):
        a1 = np.array([1,2,3])
        a2 = [1,2,3]
        comparer = ExactArrayComparer()
        with self.assertRaises(AssertionError):
            comparer(a1,a2)

class TestSymmetric(unittest.TestCase):

    def test_scalars(self):
        comparer = SymetricArrayComparer(RTOL)
        self.assertTrue(comparer.are_equal(ZERO,ZERO))
        self.assertFalse(comparer.are_equal(ONE,ZERO))
        self.assertFalse(comparer.are_equal(ZERO,ONE))
        self.assertFalse(comparer.are_equal(PICO+ONE,PICO))
        self.assertFalse(comparer.are_equal(PICO,PICO+ONE))
        self.assertTrue(comparer.are_equal(TERA,TERA+PICO))
        self.assertTrue(comparer.are_equal(TERA+PICO,TERA))

    def test_equal(self):
        a1 = np.array( [1,2,3] )
        a2 = np.array( [1,2,3] )
        comparer = SymetricArrayComparer(RTOL)
        comparer(a1,a2)

if __name__ == '__main__':
    unittest.main()
