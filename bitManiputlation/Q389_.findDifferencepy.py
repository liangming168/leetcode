# -*- coding: utf-8 -*-
"""
Q389 find the difference
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
"""

"""
method 
bit manipulation, since s and t share n-1 same letters, then ther will be 1 left single in t

time complexity: O(n), iterate all the t
space complexity: O(1)
"""
class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        a = 0
        for i in range(len(s)):
            a = a^ord(s[i])^ord(t[i])
        a ^= ord(t[len(s)])
        return chr(a)  
if __name__=="__main__":
    print(Solution().findTheDifference('qbcd','qcdbt'))
    
    