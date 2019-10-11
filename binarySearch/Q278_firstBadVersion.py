# -*- coding: utf-8 -*-
"""
Q278 first bad version
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 
"""

'''
method 1 binary search
a is the start, b is the end
mid = (a+b)//2, if isBadVersion(mid)==True, it should be in [a,mid],update b=mid
if isBadVersion(mid)==False, it should be in [mid+1,b], a = mid+1
when is not a<b stop
at last, if mid is the result, b=mid, and since a=b now, a=b=mid
         if mid+1 is the result, then a is the reuslt
so return a


time complexity: O(lgn)
space complexit: O(1)
'''

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1
        if not isBadVersion(n) or n==0:
            return None
        a = 1 # THE range is 1,2,3,...,n
        b = n
        while a<b:
            mid = (a+b)//2
            if isBadVersion(mid):
                b = mid
            else:
                a = mid + 1
        return a