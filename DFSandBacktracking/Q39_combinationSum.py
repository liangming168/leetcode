# -*- coding: utf-8 -*-
"""
Q39 Combination Sum

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

'''
method dfs backtracking
use remainder to keep next target, remainder[0]=target, remainder = remainder - candidates[j]
iterate candidates[j], push candidates[j] to curr, update remainder go next dfs
after this level done, pop candidates[j]

if remainder == 0, find the resuslts, attach curr to res
else if remainder <0 , no result, resturn None

note: attach curr[:] to res, shallow copy
directly update remainder in dfs(*,*,*，remainder-candidates[j]), to avoid conflict in different copy depth
this problem can use one number duplicate, so don't increase j for next dfs

time: O((n+k)!), n is size of candidates and k is the max duplitaction for each num,
space: O(n+k), the depth of the recursion 
'''


class Solution:
    
    def __init__(self):
        self.res = []
        
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.dfs(candidates,0,[],target)
        return self.res
        
    def dfs(self,candidates,i, curr, remainder):
        if remainder == 0:
            self.res.append(curr[:])
            return
        if remainder < 0:
            return 
        for j in range(i,len(candidates)):
            curr.append(candidates[j])
            self.dfs(candidates,j,curr, remainder - candidates[j])
            curr.pop()