# -*- coding: utf-8 -*-
"""
Q22 generate parentheses
@author: Ming Liang

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
'''
mehtod dfs backtracking
use left and right to record the remeaining '(' and ')'
if left==0 and right==0, append curr to res
if left>0 we can add "(", left--
if right>left, we can add ")", right --

time: O(4^n/sqrt(n)), for naive permuatation, there are 2^(2n), upper bound 4^n
spce: O(4^n/sqrt(n)) 
'''
class Solution:
    
    def __init__(self):
        self.res = []
        
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n<=0:
            return ['']
        self.dfs(n, n,'') # left "(" remaining, right ')' remaining
        return self.res
    
    def dfs(self,left,right,curr):
        if left==0 and right==0:
            self.res.append(curr[:])
            return
        if left>0:
            self.dfs(left-1,right,curr+'(')
        if right>left:
            self.dfs(left,right-1,curr+')')
        
            