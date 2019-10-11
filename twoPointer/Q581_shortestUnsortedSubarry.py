# -*- coding: utf-8 -*-
"""
Q581 shortest unsorted subarray

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
"""
'''
method1 sort

sort the nums array and store it as tmp
find the first and last place where tmp!=nums, 
then the length of the unsorted array is last-first+1

time: O(nlgn)
space: O(n)
'''

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return 0
        tmp = sorted(nums)
        last = -1
        first = -1
        for i in range(len(nums)):
            if nums[i]!=tmp[i]:
                if last == -1:
                    first = i
                last = i
        if last!=first:
            return last-first+1
        return 0
    
'''
method 2 find the beginning and the end of the unsorted subarray
first, find the smallest/largest number in the unsorted subarray
second, based on the smallest and largest number find the left begining and the right ending

time: O(n)
space: O(1)
'''
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return 0
        flag = False
        smallest, largest = float('inf'), -float('inf')
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                flag = True
            if flag:
                smallest = min(smallest,nums[i])
        flag = False
        for i in range(len(nums)-2,-1,-1):
            if nums[i]>nums[i+1]:
                flag = True
            if flag:
                largest = max(largest,nums[i])
        for l in range(len(nums)):
            if nums[l]>smallest:
                break
        for r in range(len(nums)-1,-1,-1):
            if nums[r]<largest:
                break
        if r-l>=0:
            return r-l+1
        return 0
