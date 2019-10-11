# -*- coding: utf-8 -*-
"""
Q247 Strobogrammatic Number2

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

Example:

Input:  n = 2
Output: ["11","69","88","96"]


"""

'''
method1 two pointer
iterate to check

time complexity: O(n), O(n) for the recursive and a small number to eleminate '0' start
space complexity: O(n), depth of the recursion and usage of stack

'''

class Solution:
    def findStrobogrammatic(self, n):
        """
        :type num: str
        :rtype: bool
        """
        
        res = self.helper(n)
        if n>1:
            res = [r for r in res if r[0]!='0']
        return res
        
        
    def helper(self,n):
        table = {'0':"0","1":"1","6":"9",'9':'6','8':'8'}
        if n==0:
            return []
        if n==1:
            return ['0','1','8']
        if n==2:
            return ['00','11','69','88','96']
        if n>2:
            base = self.helper(n-2)
            
        return [k+i+table[k] for k in table for i in base]
            

    
'''
method 2 
two pointer with hashtable

time complexity: O(n*10^n), each num it use O(n), search for 10^n-10^(n-1)
space complexity: O(1), dictionary
'''
class Solution2:
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(10**(n-1)-1,10**n):
            if self.isSBG(str(i)):
                res.append(str(i))
        return res
        
        
        
    def isSBG(self,num):
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
    mySolution = Solution()
    print(mySolution.findStrobogrammatic(3))
