# -*- coding: utf-8 -*-
"""
Q202 Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

'''
method hashset
use a hashset to store the nums in process, if it appears again, return False, is square sum is 1 return True

time complexity: O(1)
space complexity: O(n)
'''

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        res = set()
        while n:
            if n in res:
                return False
            else:
                res.add(n)
            n = self.digitSquareSum(n)
            if n == 1:
                return True
        return False
    def digitSquareSum(self,n):
        squareSum = 0
        while n:
            squareSum += (n%10)**2
            n = n//10
        return squareSum