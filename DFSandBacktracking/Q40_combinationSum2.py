# -*- coding: utf-8 -*-
"""
Q40 combination sum 2

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""

'''
method 1 combination DFS
duplicated handling, to avoid duplicates, we can use a vistied matrix, 
            first sort nums, if i>0 and nums[i]==nums[i-1] and vistied[i]==0, 
            meaning avoid the previous done duplicate
            
time: O(n!)
space: O(n)
             
'''

class Solution:
    
    def __init__(self):
        self.res = []
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        visited = [0]*len(candidates)
        self.dfs(candidates,0,[],target,visited)
        return self.res
    
    def dfs(self,candidates,start,curr,remainder,visited):
        if remainder == 0:
            self.res.append(curr[:])
            return
        if remainder < 0:
            return

        for i in range(start,len(candidates)):
            if i>0 and candidates[i]==candidates[i-1] and visited[i-1]==0:
                continue
            curr.append(candidates[i])
            visited[i] = 1
            self.dfs(candidates,i+1, curr, remainder - candidates[i],visited)
            curr.pop()
            visited[i] = 0
            
if __name__ == "__main__":
    mySolution = Solution()
    print(mySolution.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))
    
'''
method 2 
to avoid duplicate, we don't use visited matrix,just set if i>start and nums[i]==nums[i-1]: continue
'''
class Solution:
    
    def __init__(self):
        self.res = []
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.dfs(candidates,0,[],target)
        return self.res
    
    def dfs(self,candidates,start,curr,remainder):
        if remainder == 0:
            self.res.append(curr[:])
            return
        if remainder < 0:
            return

        for i in range(start,len(candidates)):
            if i>start and candidates[i]==candidates[i-1]:
                continue
            curr.append(candidates[i])

            self.dfs(candidates,i+1, curr, remainder - candidates[i])
            curr.pop()

            
if __name__ == "__main__":
    mySolution = Solution()
    print(mySolution.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))    
