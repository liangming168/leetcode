# -*- coding: utf-8 -*-
"""
Q674 longest continuous increasing sequence

Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1.
"""

'''
time: O(n)
space: O(1)
'''

class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        seq_tail = nums[0]
        max_len = 1
        tmp_len = 1
        for i in range(1,len(nums)):
            if nums[i]>seq_tail:
                seq_tail = nums[i]
                tmp_len += 1
            else:
                seq_tail = nums[i]
                tmp_len = 1
            if tmp_len>max_len:
                max_len = tmp_len
                
        return max_len