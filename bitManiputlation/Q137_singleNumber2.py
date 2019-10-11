# -*- coding: utf-8 -*-
"""
Q137 single number 2
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
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
                res[num] +=1
            else:
                res[num] =1
            if res[num] == 3:
                res.pop(num)
        return list(res.keys())[0]

 

    
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
    
    