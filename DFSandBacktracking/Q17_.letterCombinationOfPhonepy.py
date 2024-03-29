# -*- coding: utf-8 -*-
"""
Q17 letter combination of phone number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""
'''
method dfs backtracking

time: O(4^n)
space: O(n)
'''
class Solution:
    def __init__(self):
        self.res =  []
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return self.res
        table = {}
        table['2'] ='abc'
        table['3'] ='def'
        table['4'] ='ghi'
        table['5'] ='jkl'
        table['6'] ='mno'
        table['7'] ='pqrs'
        table['8'] ='tuv'
        table['9'] ='wxyz'
        self.dfs(digits,table,0,'')
        return self.res
    
    def dfs(self,digits,table,start,curr):
        if start == len(digits):
            self.res.append(curr[:])
            return

        for letter in table[digits[start]]:
            curr += letter    
            self.dfs(digits,table,start+1,curr)
            curr = curr[:-1]
                
                
        