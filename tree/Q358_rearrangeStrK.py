# -*- coding: utf-8 -*-
"""
Q358 rearrange string k apart

Given a non-empty string s and an integer k, rearrange the string such that the same characters are at least distance k from each other.

All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".

Example 1:

Input: s = "aabbcc", k = 3
Output: "abcabc" 
Explanation: The same letters are at least distance 3 from each other.
Example 2:

Input: s = "aaabc", k = 3
Output: "" 
Explanation: It is not possible to rearrange the string.
Example 3:

Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least distance 2 from each other.
"""
'''
method priority queue

cnt the frequency of each letter, then put (cnt,letter) pairs into a priority queue
while queue is not empty, each time pop out min(k, len) letters out, len initialized as len(s)
once pop out, add to res='', if this letter remaining cnt >0, save it into a cache, then len--, meaning letter remaining #decrease
for all the pairs in cache, push back to priority queue for next round

note in each round check wheck pq is empty, if in a loop pq is empty, it meaning no more letter to sperate the space

note: if python, it's min-heap, so use negative value to achieve max heap 

time: O(n)
space: O(1)
'''
class Solution:
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if not s or not k:
            return s
        cnt = [0]*26
        for ch in s:
            cnt[ord(ch)-ord('a')] += 1
        myq = []
        heapq.heapify(myq)
        for i in range(len(cnt)):
            if cnt[i]>0:
                letter = chr(i+ord('a'))
                heapq.heappush(myq,(-cnt[i], letter)) # negative freq to achieve max-heap
        strLen = len(s)
        res = ''
        while myq:
            cache = [] # to store pop out pairs, whose cnt>0
            for i in range(min(k,strLen)):
                if not myq:
                    return '' #need some letter to fill the gap but no letters left
                tmp = myq[0]
                res += tmp[1]
                heapq.heappop(myq)
                if -tmp[0]-1>0:
                    cache.append((tmp[0]+1,tmp[1]))
                strLen -= 1
            for c in cache:
                heapq.heappush(myq,c)
        return res
        
                
            
            