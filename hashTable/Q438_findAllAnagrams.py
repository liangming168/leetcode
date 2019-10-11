# -*- coding: utf-8 -*-
"""
Q438 Find All Anagrams in a String
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

'''
method hash table
use a table ft[0]*26 to store the frequency of the letters in p
use another table fw = [0]*26 to keep track the letter frequency in the window size len(p)
iterate throught all the letters in s
when 1 letters in, add on this letters frequency in the fw
if the index pointer i>=len(p), the window is full and should knick the first letter frequency out
the letter at i-len(p)'s frequency should -1,
if fw = ft, return the first letter postion in the window, i-len(p)+1
[0,1,2,3,4,5,6]
[*,*,*]


time complexity: O(ns+np)
space complexit: O(1)
'''

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        ns = len(s)
        np = len(p)
        if ns<np:
            return res
        ft = [0]*26
        fw = [0]*26
        for i in range(np):  # O(np)
            ft[ord(p[i])-ord('a')] += 1
        for i in range(ns):  # O(ns)
            fw[ord(s[i]) - ord('a')] += 1
            if i>=np:
                fw[ord(s[i-np]) - ord('a')] -= 1
            if fw == ft: # O(1)
                res.append(i-np+1)
        return res
