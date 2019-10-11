# -*- coding: utf-8 -*-
"""
Q896 Monotonic Array
Created on Sun Sep 23 21:29:03 2018

@author: Ming Liang


An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.
"""
"""
method
use the ith element minus (i-1)th element as a new array B
if max(B)*min(B)>=0 it's monotonous 
     
time complexity: O(n)
space complexity: O(1)
"""

class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        if n<=1:
            return True
        for i in range(1,n):
            A[i-1] = A[i-1] - A[i]
        if min(A[:-1])*max(A[:-1])>=0:
            return True
        return False
        
        
        
        
        