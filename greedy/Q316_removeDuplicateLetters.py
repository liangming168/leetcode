# -*- coding: utf-8 -*-
"""
Q316 remove duplicate letters
"""

'''
method 1 greedy

cnt the frequency of each letter
iterate the str, use a stack to keep valid letter for result, cnt[i]--, remaining letter reduced
if str[i] is in stack, continue, 
if str[i] is in not in stack, and str[i] smaller than the top of stack and cnt[stack[-1]] >0, pop the top of stack
            while loop for the process, until no letter at top of stack is larger
            push str[i] into stack
            
time: O(n*26)
space: O(26)
'''
class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = [0]*26
        stack = []
        for ch in s:
            cnt[ord(ch)-ord('a')] += 1
        for ch in s:
            idx = ord(ch) - ord('a')
            cnt[idx] -= 1
            if ch in stack:
                continue
            else:
                # when the top of the stack is larger and there is remaining letter the same as stack[-1] in later
                while len(stack)>0 and stack[-1]>ch and cnt[ord(stack[-1])-ord('a')]>0:
                    stack.pop()
                stack.append(ch)
        return ''.join(stack)
'''
use an array of 26 letters to check whether in stack
'''

class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = [0]*26
        stack = []
        inStack = [False]*26 
        for ch in s:
            cnt[ord(ch)-ord('a')] += 1
        for ch in s:
            idx = ord(ch) - ord('a')
            cnt[idx] -= 1
            if inStack[idx]:
                continue
            else:
                while len(stack)>0 and stack[-1]>ch and cnt[ord(stack[-1])-ord('a')]>0:
                    inStack[ord(stack[-1])-ord('a')]= False
                    stack.pop()
                stack.append(ch)
                inStack[idx] = True
        return ''.join(stack)