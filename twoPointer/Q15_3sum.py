# -*- coding: utf-8 -*-
"""
Q15 three sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
'''
method2 
hash table to 3 sum, and use hashset to avoid duplicasts
finally change set to list to return


time: O(n^2), nlogn to sort, n to iterate and n to find 2 sum = n^2, but hte final mapping set to list may cost
space: O(n), hashset
'''
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n<=2:
            return []
        nums.sort()
        res = set()
        for i in range(n):
            curr = nums[i]
            target = 0 - curr
            table = {}
            for j in range(i+1,n):
                if nums[j] in table:
                    res.add((curr, table[nums[j]], nums[j]))
                else:
                    table[target - nums[j]] = nums[j]
        return [*map(list,res)]
    
"""
method2 two pointer
iterate the nums, and the target = 0 - nums[i]
while iterate we first avoid the duplicated target by using
                        if i>0 and nums[i] == nums[i-1], then contine ,i.e i++
then it becomes the 2 sum
in two sum we use l and r pointer to find the results
to avoid duplicate, if for a target we find one pairs, then l++,
                    then we use while nums[l]==nums[l-1] and l<r, then l++ to avoid the duplicated 2 pairs


time: O(n^2)
space: O(1), no extra space
"""    
    
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        if n<=2:
            return res
        nums.sort()
        for i in range(n):
            if i>0 and nums[i] ==nums[i-1]: # avoid duplicate target
                continue
            curr = nums[i]
            target = 0- curr
            l, r = i+1, n-1
            while l<r:
                if nums[l] + nums[r] == target:
                    res.append([curr,nums[l], nums[r]])
                    l += 1 # find other pairs == target
                    while l<r and nums[l] == nums[l-1]: # avoid duplicated 2 pairs
                        l += 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return res
"""
method2 hash table
sort nums first, hash table simmilar as two sum
to avoid duplicate
first avoid 3 sum duplicate, if i>0 and nums[i]==nums[i-1], coninue to next i, 
                                        this check before going into the current i

seocnd to avoid 2 sum duplicate, if 2 sum found, mark table[num[j]] as 'used',
                                if nums[j] in table and table[nums[j]] == 'used'
                                this check before going into the current j

time: O(n^2)
space: O(n), hash table
"""    
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        if n<=2:
            return res
        nums.sort()
        for i in range(n):
            if i>0 and nums[i] ==nums[i-1]: # avoid duplicate for the remaining 2 sum
                continue
            curr = nums[i]
            target = 0- curr
            table = {}
            for j in range(i+1,n):
                if nums[j] in table and table[nums[j]] == 'used':
                    continue
                if nums[j] in table:
                    res.append([curr, table[nums[j]],nums[j]])
                    table[nums[j]] = 'used'
                else:
                    table[target- nums[j]] = nums[j]
        return res