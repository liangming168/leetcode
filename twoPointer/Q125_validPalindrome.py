# -*- coding: utf-8 -*-
"""
Q125 Valid Palindrome
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""

'''
method two pointer
p1, p2 = 0, n-1
if s[p1] not a number or letter [str.isalnum()], p1 ++
if s[p2] not a number or letter, p2--
if they are both letter, change to lower to compare, 
                        if not equal, False
else: they may be two numbers or one number with one letter
                        if not equal, False


time complexity: O(n)
space complexit: O(1)
'''

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        p1, p2 = 0, len(s)-1

        while p1<p2:
            if not s[p1].isalnum():
                p1 += 1
                continue
                
            if not s[p2].isalnum():
                p2 -= 1
                continue
                
            if s[p1].isalpha() and s[p2].isalpha():
                if s[p1].lower() != s[p2].lower():
                    return False
            else:
                if s[p1] != s[p2]:
                    return False
            p1 += 1
            p2 -= 1
                
        return True