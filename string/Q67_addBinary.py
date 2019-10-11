# -*- coding: utf-8 -*-
"""
Q67 Add binary

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""
'''
method
for every bit sum with carry when a or b or carry has value
'''


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ''
        carry = 0
        n1 = len(a) -1
        n2 = len(b) -1 
        while n1>=0 or n2>=0 or carry:
            val = (n1>=0 and a[n1]=='1') + (n2>=0 and b[n2]=='1') + carry
            curr = val%2
            carry = val//2
            res = str(curr) + res
            n1 -= 1 
            n2 -= 1
        return res
            
'''
method
similar as solution above, but use True + True = 2 to replace if else check whether there is digits in a/b
'''
class Solution1:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ''
        carry = 0
        n1 = len(a) -1
        n2 = len(b) -1 
        while n1>=0 or n2>=0 or carry:
            if n1>=0:
                aSum = int(a[n1])
            else:
                aSum = 0
            if n2>=0:
                bSum = int(b[n2])
            else:
                bSum = 0
            val = aSum + bSum + carry
            curr = val%2
            carry = val//2
            res = str(curr) + res
            n1 -= 1 
            n2 -= 1
        return res
