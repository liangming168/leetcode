# -*- coding: utf-8 -*-
"""
Q409 Longest Palindrome

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""
'''
method hashset
use hashset to store char, if already in the set, remove out, else add in
after done, if len(set) is zero, return len(s), otherwise return len(s)-len(res)+1

time complexity: O(n)
space complexity: O(n)
'''

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = set()
        for i in s:
            if i in res:
                res.remove(i)
            else:
                res.add(i)
        if len(res)==0:
            return len(s)
        else:
            return len(s)-len(res)+1