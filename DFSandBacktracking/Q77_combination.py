# -*- coding: utf-8 -*-
"""
Q77 combination

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
'''
method dfs backtracking

time: O(n!), there is T(n) = nT(n-1) + kn+C, each time we find n, then n-1
space: O(n), the depth is k so, it's O(kn)=O(n)
'''


class Solution:
    
    def __init__(self):
        self.res = []
        
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.dfs(n,k,[],1)
        return self.res
    
    def dfs(self,n,k,curr,start):
        if len(curr) == k:
            self.res.append(curr[:])
            return
        for j in range(start,n+1):
            curr.append(j)
            self.dfs(n,k,curr,j+1)
            curr.pop()