# -*- coding: utf-8 -*-
"""
Q269 aline dictionary

There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
] 

Output: "" 

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
"""

'''
method topological sorting BFS

first cnt number of distinct letters, for each letter set it's indegree as 1
then build the graph, 
        compare neighbouring 2 words, find the first 2 different letter 
        the first lette as key, 2nd lette as value to be added in a hashmap
        to avoid duplicated value for each key, use hashset as value
        if new letter added into hashset, this letter's indegree add 1, avoid duplicate add on in degree
        
        
        then BFS topological sorting, 
                first use a que to store all letter in degree is 1
                if que not empty, pop (from the head) out the letter add to res
                then if the letter in table, iterate its value hashset
                    for the letter in hashset, it's degree --1, check now whether indegree==1:
                        if so, add to the tail of que
        finally check whether len of res == cnt
        
time: O(V+E), O(26*n)
space: O(1), 26 letters
'''

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if not words:
            return ''
        
        degree = [0]*26 # in degree
        cnt = 0 # num of distinct letters
        res = []
        for w in words:
            for letter in w:
                if degree[ord(letter)-ord('a')] == 0:
                    degree[ord(letter)-ord('a')] = 1
                    cnt += 1
        table = {}
        #table = {t:[j,3,4,5,7]}
        for i in range(len(words)-1):
            curr = words[i]
            next_ = words[i+1]
            for j in range(min(len(curr),len(next_))):
                if curr[j] != next_[j]:
                    if curr[j] not in table:
                        table[curr[j]] = set()
                    
                    if curr[j] in table and next_[j] not in table[curr[j]]:
                        table[curr[j]].add(next_[j])
                        degree[ord(next_[j])-ord('a')] += 1
                        
                    break # wtk vs wjt, just the 2nd postion make sense
        que = []
        for i in range(26):
            if degree[i] == 1:
                que.append(chr(i+ord('a')))
        print(degree)
        while que:
            curr_letter = que.pop(0)
            res.append(curr_letter)
            if curr_letter in table:
                for w in table[curr_letter]:               
                    degree[ord(w) - ord('a')] -= 1
                    if degree[ord(w) - ord('a')] == 1:
                        que.append(w)

        if len(res) != cnt:
            return ''
        return ''.join(res)
        
        
                        
                    