# -*- coding: utf-8 -*-
"""
Q844 Backspace String Compare
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""

'''
method 1
use stack to store string characters, if the new char is '#' and the stack [] is not empty, pop the last element

time complexity: O(m+n) , m,n is the length of S and T
space comlexity: O(m+n)

'''

class Solution1:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def strBuilder(S):
            S_stack = []             
            for s in S:
                if s=='#':
                    try:
                        S_stack.pop()
                    except:
                        pass
                else:
                    S_stack.append(s)
            return "".join(S_stack)

        return strBuilder(S) == strBuilder(T)
    # if make it a sting use: ''.join(S_stack)
            

'''
method 1
use two pointers
pointers i, j for string S, T
iterate from the back to the start of each string
if '#', skip the 1 char, and record it as skip++,i--/j--
if not '#' and skip>0, skip-- and i--/j--
else, do nothing and come out to compare the current char(s) and char(t)
                                if char(s) != char(t), return False
                                else, i--, j--
                                if i or j one is less than 0 and one is not, return False
then compare the remaining substrings

time complexity: O(m+n) , m,n is the length of S and T
space comlexity: O(1)

'''


class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        i, j = len(S)-1, len(T)-1
        while j>=0 or i>=0:      
            skip = 0
            while i>=0:
                if S[i]=='#':
                    skip += 1
                    i -= 1
                elif skip>0:
                    skip -= 1
                    i -= 1
                else:
                    break
            skip = 0
            while j>=0:
                if T[j]=='#':
                    skip += 1
                    j -= 1
                elif skip > 0:
                    skip -= 1
                    j -= 1
                else:
                    break
            if (j>=0) != (i>=0): # compare sth with nothing
                return False
            if i>=0 and j>= 0 and S[i] != T[j]: # the current valid char is not equal
                return False

            i -= 1
            j -= 1
        return True                
                    
                    
                    
                    
                    
                    
        