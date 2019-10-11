# -*- coding: utf-8 -*-
"""
Q260 single number 3
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
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
        :rtype: List[int]
        """
        res = {}
        for num in nums:
            if num in res:
                res[num] += 1
            else:
                res[num] = 1
            if res[num] == 2:
                res.pop(num)
        return list(res.keys()) 

    
"""   
method 2
bit manipulation
based on shannon theory, use 2 bits to record
a = b = 0 to begin
if a number k comes the first time,   a = k, b=0
                    the second time,  a = 0, b=k
                    the thrid time,   a= 0, b=0
            that is a = a xor k, for the 1st and 2nd k to come
                    b = b xor k, for the 2nd k to come
 
time complexity: O(n), iterate all the nums for O(n)
space complexity: O(1)
"""
class Solution2:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a, b = 0, 0
        for num in nums:
            a = a^num & ~b
            b = b^num & ~a
        return a|b
    
    