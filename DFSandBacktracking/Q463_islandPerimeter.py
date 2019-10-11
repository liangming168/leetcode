# -*- coding: utf-8 -*-
"""
Q463 Island Perimeter
Created on Sun Sep 23 21:29:03 2018

@author: Ming Liang

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
"""

"""
method 1
use dfs
iterate each (i,j) of grid
for each, use dfs, if grid[i][j]==1
if i,j hit the boundary, there perimeter++
if grid[i][j]==0 and hasn't been visited before visited[i][j]==0, perimeter++
if visited[i][j]==1, then keep perimeter unchanged
else grid[i][j]->0, visited[i][j]->1
then search 4 neigbour direcitons

time complexity: O(mn) we visit every node onces
space complexity: O(mn), for the vistied matrix
"""


class Solution1:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perim = 0
        visited = [[0]*len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perim = self.dfs(grid,visited,i,j)
                    return perim # since there is juse 1 island
        return perim

    def dfs(self,grid,visited,i,j):
        perim = 0
        if i<0 or j<0 or i>=len(grid) or j>= len(grid[0]):
            return 1
        if grid[i][j]==0 and visited[i][j]==0:
            return 1
        if visited[i][j]==1:
            return 0
        grid[i][j] = 0
        visited[i][j] = 1
        perim += self.dfs(grid,visited,i+1,j)
        perim += self.dfs(grid,visited,i-1,j)
        perim += self.dfs(grid,visited,i,j-1)
        perim += self.dfs(grid,visited,i,j+1)
        return perim

"""
method 2
since there is only 1 island, we find the place where the island hit the water, then perimeter++
upper i=0 or grid[i-1][j]==0
lower i=len(grid)-1 or grid[i+1][j]==0
left j=0 or grid[i][j-1]==0
right j=len(grid[0]) or grid[i][j+1]==0

time complexity : O(mn)
sapce complexity: O(1)
"""   

class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perim = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    if i==0 or grid[i-1][j]==0:
                        perim +=1
                    if i==len(grid)-1 or grid[i+1][j]==0:
                        perim +=1
                    if j==0 or grid[i][j-1]==0:
                        perim += 1
                    if j==len(grid[0])-1 or grid[i][j+1]==0:
                        perim += 1
        return perim