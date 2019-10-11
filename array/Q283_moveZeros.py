# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 00:29:07 2018
LeetCode Q283 move zeros
@author: Ming Liang
input: [1,2,0,3,0,0,5,7]
output: [1,2,3,5,7,0,0,0]
"""

'''
method 1
use p to iterate from 0 to n-1, steps = 0 to record movement from current 0 to next non-zero element
                                or steps can be treated as numbers of 0s encounter
if nums[p] is 0, steps++, p++ as loop goes
else nums[p-steps] and nums[p] exchange
stop: for loop p from 0 to n-1

time complexity: O(n)
space comlexity: O(1)

'''



class Solution1:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        steps = 0
        for p in range(n):
            if nums[p]==0:
                steps += 1
            else:
                tmp = nums[p-steps]
                nums[p-steps] = nums[p]
                nums[p] = tmp # if nums[p] = 0 then [123] will output [0]
        
        
        
        
'''
method 2
use 2 pointers p1 and p2 to record 
if nums[p1] == 0 and nums[p2] !=0 ,exchange them and p1++, p2++
if nums[p1] == 0 and nums[p2] ==0, p2++
if nums[p1] != 0 and nums[p2] !=0, p1++, p2++
if nums[p1] != 0 and nums[p2] == 0, p1=p2, p2++
stop  p2<n

time complexity : O(n)
space complexity: O(1), inplace change
'''



class Solution2:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p1 = 0
        p2 = 1
        while (p2<n):
            if nums[p1] == 0 and nums[p2] != 0:
                nums[p1] = nums[p2]
                nums[p2] = 0
                p1 += 1
                p2 += 1
            elif nums[p1] == 0 and nums[p2] == 0:
                p2 += 1
            elif nums[p1] != 0 and nums[p2] !=0:
                p1 +=1
                p2 +=1
            else:
                p1 = p2
                p2 += 1