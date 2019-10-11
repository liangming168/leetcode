# -*- coding: utf-8 -*-
"""
Q49 group anagram

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""

'''
method 1 hash table, sorted string as key

time: O(nklogk), sort klogk, n words
space: (nk), table used
'''

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []
        table = {}
        for s in strs:
            anagram = ''.join(sorted(s))
            if anagram not in table:
                table[anagram] = []
            table[anagram].append(s)
            
        res = []
        for t in table:
            res.append(table[t])
            
        return res
    
'''
method 2 hash table, [0]*26 cnt the letters to represent the key

time: O(nk), n # of words, k length of words
space: O(nk)
'''

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []
        table = {}
        for s in strs:
            cnt = [0]*26
            for ch in s:
                cnt[ord(ch)-ord('a')] += 1
            key = tuple(cnt)
            if key not in table:
                table[key] = []
            table[key].append(s)

        res = []
        for t in table:
            res.append(table[t])
        return res