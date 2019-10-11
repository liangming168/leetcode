# -*- coding: utf-8 -*-
"""
Q90 subsets 2

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
'''
method dfs
to avoid duplicate, in the for loop, for i in range(start,len(nums)), we need to check
                                    if i>start and nums[i] == nums[i-1] continue
                                    
time: O(2^n)
space: O(2^n)
'''


class Solution:
    def __init__(self):
        self.res = [[]]
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return self.res
        nums.sort()
        self.dfs(nums,start=0,curr = [])
        return self.res
    
    def dfs(self,nums,start,curr):
        for i in range(start,len(nums)):
            if i>start and nums[i]==nums[i-1]:
                continue
            curr.append(nums[i])
            self.res.append(curr[:])
            self.dfs(nums,i+1,curr)
            curr.pop()