# -*- coding: utf-8 -*-
"""
Q300 longest increasing subsequence

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""

'''
method 1 DP
dp[i]: the longest increasing subsequence that ending in nums[i]

time: O(n^2)
space: O(n)
'''

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return len(nums)
        dp = [1]*len(nums)
        maxLen = 1
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
            maxLen = max(dp[i],maxLen)
        return maxLen


'''
method 2 binray search

[10,9,2,5,3,7,101,18]
use tmp= [10] to keep track of a seq that is the same length as nums[0:i]
tmp =     [10], [9],  [2],   [2,5]   [2,3]   [2,3,7],  [2,3,7,101],    [2,3,7,18]
nums[i]    10    9    2       5      3       7         101               18
use BS to find the postion of nums[i] in tmp to maintain the increasing order (fitst num that is larger than nums[i])
time: O(nlogn)
space: O(n)
''' 
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return len(nums)
        tmp = [nums[0]]
        for i in range(1,len(nums)):
            l, r = 0, len(tmp)-1
            while l<r:
                mid = (l+r)//2
                if tmp[mid]<nums[i]:
                    l = mid + 1
                else:
                    r = mid
            if tmp[l]<nums[i]:
                tmp.append(nums[i])
            else:
                tmp[l] = nums[i]
        
        return len(tmp) 