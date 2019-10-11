# -*- coding: utf-8 -*-
"""
Q200 Number of Islands
Created on Sun Sep 23 21:29:03 2018
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""

"""
method 
it's same as island area

note: input is string "1" and "0"

time complexity: O(mn) we visit every node onces
space complexity: O(1)
"""

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not any(grid):
            return 0
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    self.dfs(grid,i,j)
                    num += 1  
        return num
    
    def dfs(self,grid,i,j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
            return
        if grid[i][j]=="0":
            return
        grid[i][j] = "0"
        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j-1)
        self.dfs(grid,i,j+1)
        return
    
if __name__=="__main__":
    mySolution = Solution()
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    print(mySolution.numIslands(grid))
    
    