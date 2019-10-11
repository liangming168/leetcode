# -*- coding: utf-8 -*-
"""
Q193 word break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""
'''
mehtod 1 BFS
time: O(2^n)
'''
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return True,
        table = set(wordDict)
        curr = [s]
        next_ = []
        while curr:
            for curr_str in curr:
                for i in range(len(curr_str)):
                    if curr_str[:i+1] in table:
                        if i==len(curr_str)-1:
                            return True
                        next_.append(curr_str[i+1:])  
            
            curr = next_
            next_ = []
        return False          
'''
mehtod 2 DFS
time: O(2^n)
'''
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return True
        table = set(wordDict)
        if self.dfs(table,s):
            return True
        return False
    
    def dfs(self,table,s):
        for i in range(len(s)):
            if s[:i+1] in table:
                if i==len(s)-1:
                    return True
                if self.dfs(table,s[i+1:]):
                    return True
        return False
'''
method 3 DP
define dp[i] is True if dp[j] is True and s[j:i] is in table, dp[0]= True, len(dp)= len(S)+1
           j  i
       'dogcat'
       ['dog','cat']
       [1,0,0,1,0,0,1]
time: O(n^2)
space: O(n)
'''

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return True
        table = set(wordDict)
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(1,len(s)+1):
            for j in range(0,i):
                if dp[j] and s[j:i] in table:
                    dp[i] = True
                    break
        return dp[-1]        