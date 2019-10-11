# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 15:51:34 2018
Q78 subsets


Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

'''
method 1 iterate and add new element to previous temperary results

time: O(2^n), all possible numbers of subsets are 2^n=C(n,0)+C(n,1)+C(n,2)+...+C(n,n)
space: O(2^n), 
'''

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums)==0:
            return nums

        res = [[]]
        for i in nums:
            temp = res
            for j in range(len(temp)):
                add = temp[j]+[i]
                res.append(add)
        return res
    
    
'''
method 2 dfs, res = [[]], 

time: O(2^n)
space: O(2^n), 
'''

class Solution1:
    
    def __init__(self):
        self.res = [[]]
    
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums)==0:
            return self.res
        self.dfs([],0,nums)
        return self.res

    def dfs(self,curr,start,nums):
        for i in range(start,len(nums)):
            curr.append(nums[i])
            self.res.append(curr[:])
            self.dfs(curr,i+1,nums)
            curr.pop()
        return
if __name__=="__main__":
    mySolution = Solution1()
    print(mySolution.subsets([1,2,3]))