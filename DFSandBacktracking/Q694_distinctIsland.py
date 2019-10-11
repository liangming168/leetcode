# -*- coding: utf-8 -*-
"""
Q694 number of distinct island
Created on Sun Sep 23 21:29:03 2018
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.
Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.
"""

"""
method 
it's similar as number of island
use dfs to search each island, and store the shape of the island
use a string to track the search sequence, 'r','l','d','u' for the 4 direciton, 'b', island with the same 
shape would have the same string
then store the string to a hash set, to store distinct shape, return the lenght of the hashset
 
time complexity: O(mn) we visit every node onces
space complexity: O(mn)
"""
class Solution:
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not any(grid):
            return 0
        
        res = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    string = self.dfs(grid,i,j,'o','')
                    res.add(string)
                    print(string)
                    string = ''
        return len(res)
        
    def dfs(self,grid,i,j,direction,string):
        string = ''
        if i<0 or j<0 or i>= len(grid) or j>=len(grid[0]):
            return ''
        if grid[i][j] == 0:
            return ''
        grid[i][j] = 0
        string += direction
        string += self.dfs(grid,i-1,j,'u',string) # go up
        string += self.dfs(grid,i+1,j,'d',string) # down
        string += self.dfs(grid,i,j-1,'l',string) # left
        string += self.dfs(grid,i,j+1,'r',string) # right
        string += 'b' # go back
        return string
    
if __name__=="__main__":
    mySolution = Solution()
    grid = [[1,1,1,1,0],[1,1,0,1,1],[1,1,0,0,0],[0,0,0,0,0]]
    grid2 = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
    grid3 = [[0,0]]
    print(mySolution.numDistinctIslands(grid))
    
    