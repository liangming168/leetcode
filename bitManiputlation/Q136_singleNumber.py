# -*- coding: utf-8 -*-
"""
Q136 single number
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

"""
method 1
use a hash table to store the {num: freq} if freq pop num out, then the only 1 key is the result
 
time complexity: O(n), iterate all the nums for O(n), search whether num in res for another O(1), hash table
if we use res as list to append, and search it will use anohter O(n), then it's (n^2)
space complexity: O(n)
"""
class Solution1:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = {}
        for num in nums:
            if num in res:
                res[num] += 1
            else:
                res[num] = 1
            if res[num] ==2:
                res.pop(num)
        return list(res.keys())[0]

"""   
method 2
use a hash table to store the {num: freq} 
try: pop out num, if not except: add {num:1}
 
time complexity: O(n), iterate all the nums for O(n)
space complexity: O(n)
"""
class Solution2:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = {}
        for num in nums:
            try:
                nums.pop(num)
            except:
                res[nums] = 1
        return list(res.keys())[0]
    
"""   
method 2
bit manipulation
a xor 0 = a, a xor a = 0
exchange and  combination: a xor b xor a = (a xor a) xor b= 0 xor b = b
 
time complexity: O(n), iterate all the nums for O(n)
space complexity: O(1)
"""
class Solution3:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for num in nums:
            a = a ^ num
        return a
    
    