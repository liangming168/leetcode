# -*- coding: utf-8 -*-
"""
Q695 max area of island
Created on Sun Sep 23 21:29:03 2018

@author: Ming Liang

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""

"""
method 
use dfs
iterate each (i,j) of grid
for each, use dfs, if grid[i][j]==1, then area++ and plus it's 4 direction area
if i,j hit the boundary or grid[i][j]==0, return 0

note: if grid[i][j] has been visited, set it as 0 to avoid repeat visti, and it will not influence later search 
 
time complexity: O(mn) we visit every node onces
space complexity: O(1)
"""


class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = self.dfs(grid,i,j)
                if area>res:
                    res = area
        return res
    def dfs(self,grid,i,j):
        area = 0
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
            return 0
        if grid[i][j]==0:
            return 0
        grid[i][j] = 0
        area = area + 1+ self.dfs(grid,i-1,j) + self.dfs(grid,i+1,j) + self.dfs(grid,i,j-1) + self.dfs(grid,i,j+1)

        return area
    