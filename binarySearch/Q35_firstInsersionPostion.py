# -*- coding: utf-8 -*-
"""
Q35 first insersion position
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
"""

'''
method 1 binary search
a is the start, b is the end
mid = (a+b)//2, if find in mid, return mid
if if mid > target, then , b=mid
esle, a = mid
if |a-b|==1, stop, and return b


time complexity: O(lgn)
space complexit: O(1)
'''

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or target<=nums[0]:
            return 0
        if target>nums[-1]:
            return len(nums)
        l, r = 0, len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[mid]<target:
                l = mid+1
            else:
                r = mid
        return l