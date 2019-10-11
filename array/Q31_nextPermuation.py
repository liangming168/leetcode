# -*- coding: utf-8 -*-
"""
Q31 next permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""



'''
method 
        1 5 7 2 8
     >  1 5 7 8 2
            ^    
              ^
        1 5 8 7 2
              ^ ^      
        1 5 8 2 7
from right to left, find the first element that is smaller that it's right, index = p
from right to left, find the first element is larger than nums[p], index = q
if p is None, it indicates the sequence is non-increasing, so return a non-decreasing one
else, exchange nums[p] and nums[q], reverse nums[p+1：end]

time: O(n)
space: O(1)
'''

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        '''
        1 5 7 2 8
     >  1 5 7 8 2
            ^    
              ^
        1 5 8 7 2
              ^ ^      
        1 5 8 2 7
        '''
        if not nums:
            return []
        firstSmall = None
        for i in range(len(nums)-1,0,-1):
            if nums[i-1]<nums[i]:
                firstSmall = i-1
                break
        if firstSmall is None:
            return self.reverse(0,len(nums)-1,nums)
        for i in range(len(nums)-1,-1,-1):
            if nums[i] > nums[firstSmall]:
                firstLarge = i
        self.swap(firstSmall, firstLarge, nums)
        self.reverse(firstSmall+1, len(nums)-1,nums)
        
    def swap(self,i,j,nums):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
        
    def reverse(self,i,j,nums):
        while i<j:
            self.swap(i,j,nums)
            i += 1
            j -= 1