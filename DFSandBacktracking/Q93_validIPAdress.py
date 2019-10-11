# -*- coding: utf-8 -*-
"""
Q93 valid IP address

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""

'''
method dfs backtracking
if just 1 num check any 0~9 is possible, go next dfs
if 2 num digits, check whether start with 0
if 3 num digits, check whether start with 0 and whole 3 digits <=255

before each digits iteration i=1,2,3, check when i<=len(s), the remaining length is enough

next dfs -> dfs(s[i:], index+1,curr+s[:i]+'.')

when all 4 parts got, index==4 and there is no remaining s, append curr[:-1] to res

time： O(2^n), for length n, there are (n-1) space to check , but we just check at most n=4*3, so 
                at most O(2^11)
space: O(1), at most 4 layer slacks
'''
class Solution:
    def __init__(self):
        self.res = []
    
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.dfs(s,0,'')
        return self.res
        
    def dfs(self,s,index,curr):
        if index==4:
            if not s: #no remaining string
                self.res.append(curr[:-1])
            return
        for i in range(1,4):
            if i<=len(s):
                if i == 1 or\
                (i==2 and int(s[0])!=0) or\
                (i==3 and int(s[0])!=0 and int(s[:i])<=255):
                    self.dfs(s[i:],index+1,curr+s[:i]+'.')