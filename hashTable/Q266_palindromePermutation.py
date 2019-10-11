# -*- coding: utf-8 -*-
"""
Q266 Palindrome Permutation
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:a

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
"""
'''
method hashtable
use a hashset to store the char
if it's already in the hashset, remove that out, otherwise add in
after done, check whether the length of the set is <= 1

time complexity: O(n)
space complexity: O(n)
'''

class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = set()
        for i in s:
            if i in res:
                res.remove(i)
            else:
                res.add(i)
        return len(res)<=1