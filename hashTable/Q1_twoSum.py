# -*- coding: utf-8 -*-
"""
Q1 Two sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""
'''
method hash table
use a hash table to store the result pairs,
if a new num comes, put it's contemperary part: target- num as key, current idx as value
then next num comes, if it's in the key, find the results, return the key/value pairs

time complexity: O(n)
space complexity: O(n)
'''

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in table:
                return [table[nums[i]],i]
            else:
                table[target - nums[i]] = i
        return None

