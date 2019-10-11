# -*- coding: utf-8 -*-
"""
Q680 valid Palindrome
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
"""

'''
method 2 pointer
p1, p2 = 0, len(s)
if s[p1]== s[p2], p1++, p2--
else we can have  p1++ and p2 have the subsring to compare the remaining s[p1] and s[p2] if it's return true
     also we can move at the right sidt as
                 p1 and p2++, and compare s[p1] and s[p2]
                 
time complextiy: O(n)
space complexity: O(1)
'''

class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p1, p2 = 0, len(s)-1
        if not s or len(s)<=2:
            return True
        while p1<=p2:
            if s[p1] == s[p2]:
                p1 += 1
                p2 -= 1
                # [****,XXXXXXXXXXXXXXXXXXXXXXXXXXXX,****]
            else:
                # shift 1 postion at the left side
                a = p1 + 1
                b = p2
                while  a<=b and s[a]==s[b]:
                    a += 1
                    b -= 1
                if a>=b:
                    return True
                    
                # shift 1 postion at right side
                a = p1
                b = p2 -1
                while a<=b and s[a]==s[b]:
                    a += 1
                    b -= 1
                if a>=b:
                    return True
            
                return False
        return True