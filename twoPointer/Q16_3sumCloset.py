# -*- coding: utf-8 -*-
"""
Q16 3 sum closet

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


'''
method 2 pointer
sort the nums
outer loop iterate from i = 0 to n-2, inner loop from i+1 to n-1,
if the 3 num sum to target, return 
else, find the abs difference update the newest diff and set the sum as a target result
then if sum3 < target, left ++, else right-- 

time: O(n)
space: O(1)
'''
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)< 3:
            return None
        nums.sort()
        thresh = float('inf')
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l<r:
                sum3 = nums[i] + nums[l] + nums[r]
                if sum3 == target:
                    return target
                diff = abs(sum3-target)
                if diff<thresh:
                    thresh = diff
                    res = sum3
                if sum3>target:
                    r -= 1
                else:
                    l += 1
        return res
                    
                