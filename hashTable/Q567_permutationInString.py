# -*- coding: utf-8 -*-
"""
Q567 Permutation in String
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""

'''
method hash table and sliding window
use a table ft[0]*26 to store the frequency of the letters in s1
use another table fw = [0]*26 to keep track the letter frequency in the window size len(s1)
iterate throught all the letters in s2
when 1 letters come in, add on this letters frequency in the fw
if the index pointer i>=len(s1), the window is full and should knick the first letter frequency out
the letter at i-len(s1)'s frequency should -1,
if fw = ft, return true
[0,1,2,3,4,5,6]
[*,*,*]


time complexity: O(ns+np)
space complexit: O(1)
'''

class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if not s1:
            return True
        elif not s2:
            return False
        nt = len(s1)
        ns = len(s2)
        ft = [0]*26
        fs = [0]*26
        for i in range(nt):
            ft[ord(s1[i]) - ord('a')] += 1
        for i in range(ns):
            fs[ord(s2[i]) - ord('a')] += 1
            # [0,1,2,3,4,5]
            # [*,*,*]
            if i >= nt:
                fs[ord(s2[i-nt]) - ord('a')] -= 1
            if fs == ft:
                return True
        return False