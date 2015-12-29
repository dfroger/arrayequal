#!/usr/bin/env python
import unittest

import numpy as np

from . import comparer

_exact_comparer = comparer.ExactArrayComparer()
_almost_comparer = comparer.SymetricArrayComparer()

class NumTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.addTypeEqualityFunc(np.ndarray, 'assertArrayEqual')

    def _compare_arrays(self,a1,a2,comparer,msg,astype=None):
        if astype:
            a1 = np.array(a1, astype)
            a2 = np.array(a2, astype)
        try:
            comparer(a1, a2)
        except AssertionError as e: 
            standardMsg = str(e)
            self.fail(self._formatMessage(msg, standardMsg))

    def assertArrayEqual(self, a1, a2, msg=None, astype=None):
        self._compare_arrays(a1,a2,_exact_comparer,msg,astype=astype)

    def assertArrayAlmostEqual(self, a1, a2, comparer=_almost_comparer,
                               msg=None, astype=None):
        self._compare_arrays(a1,a2,comparer,msg,astype=astype)
