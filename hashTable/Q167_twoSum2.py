# -*- coding: utf-8 -*-
"""
Q167 two sum II input is sorted
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""

'''
method1 hashtable
time: O(n)
space: O(1)
'''
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = {}
        nums = numbers
        n = len(nums)
        for i in range(n):
            if nums[i] in table:
                return [table[nums[i]]+1,i+1]
            else:
                table[target - nums[i]] = i
        return None
    
'''
method2 two pointer
time: O(n)
space: O(1)
'''
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        p1, p2 = 0, len(numbers)-1
        while p1<p2:
            if numbers[p1] + numbers[p2] == target:
                return [p1+1,p2+1]
            elif numbers[p1] + numbers[p2] < target:
                p1 += 1
            else:
                p2 -= 1
'''
method2 binary search
time: O(nkogn)
space: O(1)
'''
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            l, r = i+1, len(numbers)-1
            while l<=r:
                mid = (l+r)//2
                if numbers[mid] == tmp:
                    return [i+1,mid+1]
                elif numbers[mid] > tmp:
                    r = mid - 1
                else:
                    l = mid + 1
        return None
                
                
            