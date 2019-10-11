# -*- coding: utf-8 -*-
"""
Q128 Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 3, 200, 1, 4, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""
'''
method 1 sort and find the consecutive increasing in neigobour
time: O(nlogn)
'''

'''
method 2 hash

use a hash set to store the number
first for the consecutive sequence, find it's head, us if nums[i]-1 in set(), if not in it's the head
then set the begin k= nums[i], while k+1 in set going on, for this consecutive epoch, the length is k-nums[i]

time: O(n), for the while check loop, it's O(1)
space: O(n)
'''
class Solution:
    def findConsecutiveSeq(self,nums):
        if not nums:
            return 0
        if len(nums)==1:
            return 1
        res = 0
        s = set(nums)
        for i in range(len(nums)):
            if nums[i]-1 is not in s: # find the beginning of the consecutive seq
                k = nums[i]
                while k in s:
                    k += 1
                res = max(res,k-nums[i])
        return res
