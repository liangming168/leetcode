# -*- coding: utf-8 -*-
"""
Q304 range sum 2D

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
"""

'''
method dp
use dp[i][j]: the sum from [0][0] to [i-1][j-1]

[row1][col1]->[row2][col2] area sum is the +- of pivot points


*************
            *
            *
            *
*************
*************

time: O(1) each call
space: O(1) each call
'''
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            return None
        self.res = 0
        self.m = len(matrix)
        self.n = len(matrix[0])
        # dp[i][j]: the area from[0][0] to [i-1][j-1]
        self.dp = [[0]*(self.n+1) for _ in range(self.m+1)]
        for i in range(1,self.m+1):
            for j in range(1,self.n+1):
                self.dp[i][j] = self.dp[i-1][j] + self.dp[i][j-1]\
                                       + matrix[i-1][j-1] - self.dp[i-1][j-1] # minus overlap
        '''
         
         *******
         *******
              *
         * * **
         *******
        '''       
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        a = self.dp[row2+1][col2+1]
        b = self.dp[row1][col1]
        c = self.dp[row1][col2+1]
        d = self.dp[row2+1][col1]
        return a-c-d+b


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)