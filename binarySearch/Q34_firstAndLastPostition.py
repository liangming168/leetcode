# -*- coding: utf-8 -*-
"""
Q34 Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

'''
method 1 binary search
a is the start, b is the end
first to find the 1st element >= target,
second to find the 1st element > target
if first and second is the same, no target in nums
else return [first, second-1]


time complexity: O(lgn)
space complexit: O(1)
'''

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        if not nums:
            return [-1,-1]
        l = 0
        r = n #set the right hand as n instead of n-1 to make sure the case target ending at the last element
        while l<r: # find the first element >= target
            mid = (l+r)//2
            if nums[mid]>=target:
                r = mid
            else:
                l = mid + 1
        first = l
        l, r = 0, n
        while l<r: # findt the first element > target
            mid = (l+r)//2
            if nums[mid]>target:
                r = mid
            else:
                l = mid + 1
        second = l
        if first<second:
            return [first, second-1]
        return [-1,-1]