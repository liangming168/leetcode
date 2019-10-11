# -*- coding: utf-8 -*-
"""
Q301  remove invalid patenthesis
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""

'''
mehtod dfs

first use a cnt to check wether the string is valid, if '(', cnt++, if ')', cnt--, at current ith iteration
                                                        if cnt<0, return False, finally, check cnt==0
                                                        
second, find out num of left and right hand paprenthesis to delete
        if '(', l++, if l<=0 and ')', r++, if l>0 and ')': l--
    
then dfs to try every ch of the string
if the dfs, if l==0 and r==0 and the string is valid, append the string to result
then iterate the string, delete the current ch, then go to next ch and update r/l corresponding ch delete

note: in the dfs iteration ,only ch=='(' or ch==')' to check, and make of copy curr = s, beause we need inplace 
delete the string. 

time: O(2^n), O(2^(l+r)), each ch to check delete or not, and l==0 and r==0 to bound 
space: O(n), depth of recursion
'''

class Solution:
    def __init__(self):
        self.res = []
        
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return [""]
        if self.isValid(s):
            return [s]
        (l,r) = self.numToDelete(s)
        self.dfs(s,0,l,r)
        return self.res
        
    def dfs(self,s,start,l,r):
        if l==0 and r==0:
            if self.isValid(s):
                self.res.append(s[:])
            return 

        for i in range(start,len(s)):
                
            if i>start and s[i]==s[i-1]:
                continue # avoid duplicate
            if s[i] == "(" or s[i]==")":
                if r>0 and s[i]==')':
                    self.dfs(s[0:i]+s[i+1:],i,l,r-1)
                elif l>0 and s[i]=='(':
                    self.dfs(s[0:i]+s[i+1:],i,l-1,r)
                
        
    def isValid(self,s):
        if not s:
            return True
        cnt = 0
        for ch in s:
            if ch=='(':
                cnt += 1
            if ch==')':
                cnt -= 1
            if cnt<0: #')' is more than '('
                return False
        return cnt==0
    
    def numToDelete(self,s):
        l, r = 0, 0
        for ch in s:
            l += (ch=='(')
            if l<=0:
                r += (ch==')')
            else:
                l -= (ch==')')
        return (l,r)