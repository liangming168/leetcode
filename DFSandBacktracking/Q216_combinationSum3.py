# -*- coding: utf-8 -*-
"""
Q216 combine sum 3

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""

'''
method dfs
if len(curr)==k, then if remainder == 0, res.append(curr), else, return None

time: O(n!)
space: O(n)
'''

class Solution:
    def __init__(self):
        self.res = []
        
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.dfs(k,1,[],n)
        return self.res
    
    def dfs(self,k,start,curr,remainder):
        if len(curr)==k:
            if remainder == 0:
                self.res.append(curr[:])
                return
            else:
                return
        for i in range(start,10):
            curr.append(i)
            self.dfs(k,i+1,curr,remainder-i)
            curr.pop()
        