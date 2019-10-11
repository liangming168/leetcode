# -*- coding: utf-8 -*-
"""
Q242 Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

'''
use a hash table, to cnt the number of each word,
for letter in s we cnt++, then for the letter in t we cnt--
after that, we check whether all the values of the table is 0

time complexity: O(n), 
space complexit: O(1), the table we use is fixed
'''

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n1 = len(s)
        n2 = len(t)
        if n1 != n2:
            return False
        cnt = {i:0 for i in range(26)}
        for i in range(n1):
            cnt[ord(s[i])-ord('a')] += 1
            cnt[ord(t[i])-ord('a')] -= 1

        for i,v in cnt.items():
            if v != 0:
                return False
        return True
if __name__ == "__main__":
    s = 'abcd'
    t = 'cbad'
    print(Solution().isAnagram(s,t))
'''
method2 use list to achieve hash table
'''

class Solution2:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n1 = len(s)
        n2 = len(t)
        if n1 != n2:
            return False
        cnt1 = [0]*26
        cnt2 = [0]*26
        for i in range(n1):
            cnt1[ord(s[i])-ord('a')] += 1
            cnt2[ord(t[i])-ord('a')] += 1

        return cnt1 == cnt2
if __name__ == "__main__":
    s = 'abced'
    t = 'cbavd'
    print(Solution().isAnagram(s,t))