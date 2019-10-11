# -*- coding: utf-8 -*-
"""
Q347 topK frequent element

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
'''
method priority q

use pq to store (freq,key) pairs
and in the result pop out the smallest first, add new pop out result to the head of result

time: O(nlongk)
space: O(n)
'''
import heapq
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        table = {}
        for num in nums:
            if num in table:
                table[num] += 1
            else:
                table[num] = 1

        que = []
        heapq.heapify(que)
        for key,freq in table.items():
            if len(que)<k:
                heapq.heappush(que,(freq,key))
            else:
                if freq>que[0][0]:
                    heapq.heappop(que)
                    heapq.heappush(que,(freq,key))
        res = []
        for i in range(len(que)):
            res = [heapq.heappop(que)[1]] + res
        return res