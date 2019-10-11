# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 00:29:07 2018
LeetCode Q2344  reverse string
@author: Ming Liang


Input: "hello"
Output: "olleh"


Input: "A man, a plan, a canal: Panama"
Output: "amanaP :lanac a ,nalp a ,nam A"
"""

'''
method 1

time complexity: O(n)
space comlexity: O(n)

'''



class Solution1:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        b = ''
        for i in range(n):
            b += s[n-1-i]
            
        return b
        
