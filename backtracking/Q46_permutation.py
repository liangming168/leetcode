# -*- coding: utf-8 -*-
"""
Q46 Permutaion
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]


@author: Ming Liang
"""

'''
time compelxity: O(n!), for the recursively we call n*(n-1)*(n-2)*1
space complexity: O(n)
'''

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<=1:
            return [nums]
        curr = []
        res = []
        visited = [0] *len(nums)
        self.backtracking(curr,res,nums,visited)
        return res
    
    def backtracking(self,curr,res,nums,visited):
        if len(curr) == len(nums):
            res.append(curr[::])
            return
        
        for i in range(len(nums)):
            if not visited[i]:
                visited[i] = 1
                curr.append(nums[i])
                self.backtracking(curr,res,nums,visited)
                visited[i] = 0
                curr.remove(nums[i])
                
               
#if __name__ == '__main__':
#    mySolution = Solution()
#    print(mySolution.permute([1,2,3]))
    
    
'''
put res as instance varaible self.res in  __init__
time compelxity: O(n!), for the recursively we call n*(n-1)*(n-2)*1
space complexity: O(n)
'''

class Solution2:
    
    def __init__(self):
        self.res = []
        
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<=1:
            return [nums]
        curr = []
        visited = [0] *len(nums)
        self.backtracking(curr,nums,visited)
        return self.res
    
    def backtracking(self,curr,nums,visited):
        if len(curr) == len(nums):
            self.res.append(curr[::])
            return
        
        for i in range(len(nums)):
            if not visited[i]:
                visited[i] = 1
                curr.append(nums[i])
                self.backtracking(curr,nums,visited)
                visited[i] = 0
                curr.remove(nums[i])
                
                
if __name__ == '__main__':
    mySolution = Solution2()
    print(mySolution.permute([1,2,3]))