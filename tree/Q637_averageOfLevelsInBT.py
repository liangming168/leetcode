# -*- coding: utf-8 -*-
"""
Q637 avarage of levels in binary tree


 

Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5

"""
'''
method BFS
search each go over each level and calculate the avearge

time: O(n)
space: O(n)

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        curr = [root]
        next_ = []
        res = []
        while curr:
            tmp = []
            for c in curr:
                tmp.append(c.val)
                if c.left:
                    next_.append(c.left)
                if c.right:
                    next_.append(c.right)
            res.append(sum(tmp)/len(tmp))
            curr = next_
            next_ = []
        return res
                
        