# -*- coding: utf-8 -*-
"""
Q329 Longest increasing path in a matrix 
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""

'''
method DFS with memoization
DFS try 4 direciton, to new ni,nj, if matrix[ni][ni]>matrix[i][j], lenght++, after dfs iterate 
    put visited[(i,j)]=res length, next time if (i,j) in visited directly return result

time: O(n^2)
space: O(n^2)
'''

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        visited = {}
        self.direction = [(0,1),(0,-1),(-1,0),(1,0)]
        ans = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans,self.dfs(matrix,visited,i,j))
        return ans
    
    def dfs(self,matrix,visited,i,j):
        curr = (i,j)
        if curr in visited:
            return visited[curr]
        res = 1
        for k in range(4):
            ni, nj = i+self.direction[k][0], j+self.direction[k][1]
            if ni<0 or ni>=len(matrix):
                continue
            if nj<0 or nj>=len(matrix[0]):
                continue
            if matrix[ni][nj]<=matrix[i][j]:
                continue
            res = max(res,self.dfs(matrix,visited,ni,nj)+1)
        visited[curr] = res
        return res

if __name__ =='__main__':
    obj = Solution()
    matrix = [[9,9,4],[6,6,6],[2,1,1]]
    print(obj.longestIncreasingPath(matrix))