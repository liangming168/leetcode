# -*- coding: utf-8 -*-
"""
Q215 find the kth largest element in an array

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""


'''
method heaq queue
use heapq to store k nums if next num is larger than q[0], heap pop then push in this num

time: O(n)
space: O(1)
'''
import heapq
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        q = []
        heapq.heapify(q)
        for i in nums:
            if len(q)<k:
                heapq.heappush(q,i)
            else:
                if i>q[0]:
                    heapq.heappop(q)
                    heapq.heappush(q,i)
        return q[0]
'''
follow-up find the k largest
after find the final q
iterate the q, pop out the result and add new result to the head
'''


import heapq
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        q = []
        heapq.heapify(q)
        for i in nums:
            if len(q)<k:
                heapq.heappush(q,i)
            else:
                if i>q[0]:
                    heapq.heappop(q)
                    heapq.heappush(q,i)
        res = []
        n = len(q)
        for i in range(n):
            res = [heapq.heappop(q)] + res
        return res
    
'''
follow up: the kth largest number in streaming data

LC 703
'''
