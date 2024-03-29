# -*- coding: utf-8 -*-
"""
Q290 word pattern

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
"""
'''
method hashtable
iterate pattern and str
when key comes in check whether it's value is the same, if no key return 0
if they don't equal return False
then update the new key with the current sequence
'''
class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        p_table, s_table = {}, {}
        str_list = str.split(' ')
        if len(str_list) != len(pattern):
            return False
        for i in range(len(pattern)):
            if p_table.get(pattern[i],0) != s_table.get(str_list[i],0):
                return False
            p_table[pattern[i]] = i+1
            s_table[str_list[i]] = i+1
        return True