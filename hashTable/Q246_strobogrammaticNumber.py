# -*- coding: utf-8 -*-
"""
Q246 Strobogrammatic Number

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:

Input:  "69"
Output: true


"""

'''
method1 two pointer
iterate to check

time complexity: O(n)
space complexity: O(1)

'''

class Solution:
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if not num:
            raise(ValueError('Invalid Input'))
            return True
        p1, p2 = 0,len(num)-1
        while p1<=p2:
            if num[p1] == '0' and num[p2] == '0':
                p1 += 1
                p2 -= 1
            elif (num[p1] == '6' and num[p2] == '9') or (num[p1] =='9' and num[p2]=='6'):
                p1 += 1
                p2 -= 1
            elif (num[p1]=='1' and num[p2] =='1') or (num[p1]=='8' and num[p2]=='8'):
                p1 +=1 
                p2 -=1
            else:
                return False

        return True
    
'''
method 2 
two pointer with hashtable

time complexity: O(n)
space complexity: O(1), dictionary
'''

class Solution1:
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if not num:
            raise(ValueError('Invalid Input'))
            return True
        p1, p2 = 0,len(num)-1
        
        table = {'0':"0","1":"1","6":"9",'9':'6','8':'8'}
        while p1 <= p2:
            if num[p1] not in table or table[num[p1]]!=num[p2]:
                return False
            else:
                p1 += 1
                p2 -= 1
        return True
            
            
if __name__ == '__main__':
    mySolution = Solution1()
    print(mySolution.isStrobogrammatic('151'))
