# -*- coding: utf-8 -*-
"""
Q523 continuous subarray sum

Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42
"""


'''
method hash table
every time calculate the accumulative sum of the nums and %k, if not in table, add index to table
otherwise find the distance from current i to the same key j, if >=2 return True

Note: if k=0, just check whether there is 2 consecutive sum to 0
      initiate table={0:-1} in case the first time 2 or more cumulative sum % k is zero, e.g. [3,5]
     
time: O(n)
spce: O(1), hashtable, key just 0-9
'''
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        
        1 2 3  4  5
        1 3 6 10 15
     k=5  
     %  1 3 1  
        """
        if len(nums)<2:
            return False
        
        if k== 0:
            for i in range(len(nums)-1):
                if nums[i+1]+nums[i]==0:
                    return True
            return False
        
        table = {0:-1} 
        cumsum = 0
        for i in range(len(nums)):
            cumsum += nums[i]
            if not cumsum%k in table:
                table[cumsum%k] = i
            else:
                if i-table[cumsum%k]>1:
                    return True
        return False
                
                
                
                
                