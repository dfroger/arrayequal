#!/usr/bin/env python
import numpy as np

class ArrayComparer(object):

    def __call__(self,a1,a2): 

        # Check type.
        if not isinstance(a1, np.ndarray):
            raise AssertionError('First argument is not a numpy array')
        if not isinstance(a2, np.ndarray):
            raise AssertionError('Second argument is not a numpy array')

        # Check shape.
        s1 = a1.shape
        s2 = a2.shape
        if s1 != s2:
            raise AssertionError('arrays have different shapes: %r != %r' % (s1,s2,))

        # Check dtype
        dt1 = a1.dtype
        dt2 = a2.dtype
        if dt1 != dt2:
            raise AssertionError('arrays have different data type: %r != %r' \
                    % (dt1,dt2,))

        are_equal = self.are_equal(a1,a2)
        are_different = np.logical_not(are_equal) 

        if np.any( are_different ):
            diff1 = a1[are_different]
            diff2 = a2[are_different]
            ndiff = len(diff1)
            idx = np.where(are_different)

            if a1.size < 20:
                msg = 'arrays %s and %s have %i different value(s) at %s: %r != %r' \
                    % (a1,a2,ndiff,idx,diff1,diff2)
            elif ndiff < 20:
                msg = 'arrays have %i different value(s) at %s: %r != %r' \
                    % (ndiff,idx,diff1,diff2)
            else:
                msg = 'arrays have %i different value(s) with first at %s are: %r != %r' \
                    % (ndiff,idx[0],diff1[0],diff2[0])

            raise AssertionError(msg)

class ExactArrayComparer(ArrayComparer):

    def are_equal(self,val1,val2):
        return val1 == val2

class SymetricArrayComparer(ArrayComparer):

    def __init__(self,rtol=1e-15):
        self.rtol = rtol

    def are_equal(self,val1,val2): 
        """
        Test for equality between two floating-point numbers up to a relative tolerance
        
        Input arguments:
            val1  -- left-hand side
            val2  -- right-hand side
            rtol -- relative tolerance
            
        Output argument:
            boolean -- set to:
                true  -- if val1 and val2 are equal up to rtol
                false -- otherwise        

        TODO: check for underflow/overflow
        """
        dist = abs(val2-val1)
        amax = np.fmax(abs(val1),abs(val2))
        return dist <= self.rtol*amax
