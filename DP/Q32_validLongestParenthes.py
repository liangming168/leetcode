# -*- coding: utf-8 -*-
"""
Q32 longest valid parenthesis

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()
"""

'''
method 1 DP
use DP = [0]* len(s)
dp[i]: the longest valid longest at index i

only s[i] is ')' to check, 2 conditions
    1. if s[i-1]=='(', so dp[i] = dp[i-2] + 2
    2. if s[i-1] ==')', so we need ((    ))
        it has be s[i-dp[i-1]-1] =='(', so dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2],
        remenber to check the index >=0
    after each i, check res = max(res,dp[i])
    
time: O(n)
space: O(n)
'''
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0]*(len(s)) # dp[i]:the longest valid length at ith index
        res = 0
        for i in range(1,len(s)):
            if s[i]==')':
                if s[i-1]=='(': # '****()'
                    dp[i] = dp[i-2] + 2
                else:   # '***  * ((  *** ))'
                    if i-dp[i-1]-1 >=0 and s[i-dp[i-1]-1] == '(':
                        if i-dp[i-1]-2 >=0:
                            dp[i] = dp[i-dp[i-1]-2] + dp[i-1] +2
                        else:
                            dp[i] = dp[i-1] + 2
                res = max(res,dp[i])
        return res
'''
method scaning from left and right
1. scan from left, if '(' l++, if ')', r++, if l==r, res= max(res,r*2), if r>l, resset l=r=0
2. scan from right, reset l=r=0, similarly, except, if l>r, reset l=r=0

why left and right scan 2 times, '(()', left scan res = 0, right scan res=1

time: O(1)
space: O(n)
'''

class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        l, r = 0, 0
        for p in s:
            l += (p=='(')
            r += (p==')')
            if l==r:
                res = max(res,2*l)
            if r>l:
                r = 0
                l = 0
        
        l, r = 0, 0
        for i in range(len(s)-1,-1,-1):
            p = s[i]
            l += (p=='(')
            r += (p==')')
            if l==r:
                res = max(res,2*l)
            if l>r:
                r = 0
                l = 0
        return res
            