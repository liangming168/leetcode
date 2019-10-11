# -*- coding: utf-8 -*-
"""
Q733 Flood fill
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.

"""
"""
method
use dfs to search, up/down/left/right of the neighbour
if index(i,j) is out of valid value, return
if image[i][j] is different from the starting color or [i][j] has been visited, return
else change [i][j] to new color and mark it as visited
the reason to use visited maxtirx is that,if gird[sr][sc] color == newColor, it will become a forever loop

note: visited matrix shouldn't be as [[0]*col]*row, this will make all col changes instead of element wise 

time complexity: O(n), n is the number of elements in the image matrix
space comlexity: O(n) for additional visited matrix

space O(1) improvement, don't use visited matrix, if image[i][j]== newColor, then return

"""
    
class Solution1:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        color = image[sr][sc]
        visited = [[0 for i in range(len(image[0]))] for i in range(len(image))]
        self.dfs(sr,sc,image,color,newColor,visited)
        return image
  
    def dfs(self,i,j,image,color, newColor,visited):
        if i<0 or j<0 or i>=len(image) or j>=len(image[0]):
            return
        if image[i][j] != color or visited[i][j]==1:
            return 
        image[i][j] = newColor
        visited[i][j] = 1

        self.dfs(i-1,j,image,color,newColor,visited)
        self.dfs(i+1,j,image,color,newColor,visited)
        self.dfs(i,j-1,image,color,newColor,visited)
        self.dfs(i,j+1,image,color,newColor,visited)
if __name__ == "__main__":       
    mySolution = Solution1()
    image = [[0,0,0],[0,0,0]]
    sr, sc, newColor = 0,0,2
    mySolution.floodFill(image,sr,sc,newColor)
    
    
"""
method
use dfs to search, up/down/left/right of the neighbour
if index(i,j) is out of valid value, return
if image[i][j] is different from the starting color or [i][j] has been visited, return
else change [i][j] to new color and mark it as visited

note: visited matrix shouldn't be as [[0]*col]*row, this will make all col changes instead of element wise 

time complexity: O(n), n is the number of elements in the image matrix
space comlexity: O(n) for additional visited matrix

space O(1) improvement, don't use visited matrix, if image[i][j]== newColor, then return

"""
    
class Solution2:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        color = image[sr][sc]
        self.dfs(sr,sc,image,color,newColor)
        return image
  
    def dfs(self,i,j,image,color, newColor):
        if i<0 or j<0 or i>=len(image) or j>=len(image[0]):
            return
        if image[i][j] != color or image[i][j]==newColor:
            return 
        image[i][j] = newColor

        self.dfs(i-1,j,image,color,newColor)
        self.dfs(i+1,j,image,color,newColor)
        self.dfs(i,j-1,image,color,newColor)
        self.dfs(i,j+1,image,color,newColor)

"""
method
use dfs to search, up/down/left/right of the neighbour
same as above, but needn't to check whether image[i][j] is newColor, because if newColor == color, then
no need to do dfs, directly return

space O(1) improvement, 

"""
    
class Solution3:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        color = image[sr][sc]
        if color == newColor:
            return image
        self.dfs(sr,sc,image,color,newColor)
        return image
  
    def dfs(self,i,j,image,color, newColor):
        if i<0 or j<0 or i>=len(image) or j>=len(image[0]):
            return
        if image[i][j] != color: #no need to check whether image[i][j] == newColor
            return 
        image[i][j] = newColor

        self.dfs(i-1,j,image,color,newColor)
        self.dfs(i+1,j,image,color,newColor)
        self.dfs(i,j-1,image,color,newColor)
        self.dfs(i,j+1,image,color,newColor)  