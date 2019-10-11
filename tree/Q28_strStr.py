# -*- coding: utf-8 -*-
"""
Q28 implement of strStr()
"""

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if len(haystack)<len(needle):
            return -1
        #'abc'  'bc'
        for i in range(len(haystack)-len(needle)+1):
            if needle[0]!= haystack[i]:
                continue
            if needle == haystack[i:i+len(needle)]:
                return i
        return -1