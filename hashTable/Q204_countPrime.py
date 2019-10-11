# -*- coding: utf-8 -*-
"""
Q204 countPrime
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""


'''
method 1 check each i from [0,n-1], weahter it's prime
time complexity: O(n*sqrt(n))
space complexity: O(1)
'''
import math
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1 or not n:
            return 0
        res = 0
        for i in range(2,n):
            if self.isPrime(i):
                res += 1
        return res
        
        return res     
    def isPrime(self,n):
        for i in range(2,int(math.sqrt(n))):
            if n%i== 0:
                return False
        return True
            
if __name__ == '__main__':
    mySolution = Solution()
    print(mySolution.countPrimes(22))
    
'''
method 2
use a list [0,0]+[1]*(n-2) to store the status
then iterate i from[0,sqrt(n)+1]
if status[i] is 1, then unchecked, update [i**2],[i**2+i],[i**2+2i]...as non-prime till i**2+ki<n
time complexity: O(n*sqrt(n))
space complexity: O(n)
'''    
    
    
class Solution2:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return 0
        res = [0,0] + [1]*(n-2)
        for i in range(2,int(n**0.5)+1):
            if res[i] == 1:
                for j in range(i**2,n,i):
                    res[j] = 0
        return sum(res)