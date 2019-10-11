# -*- coding: utf-8 -*-
"""
Q543 diameter of BT

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""
'''
method recursion dfs

the diameter of the tree is the max of left subtree diameter or right subtree diameter
                                of the sum height of left and right subtree
                                
time: O(n)
space: O(h)
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
        
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.helper(root)[1]
    
    def helper(self,root):
        if not root:
            return [0,0] # height, diameter
        left = self.helper(root.left)
        right = self.helper(root.right)
        res = []
        depth = max(left[0],right[0])+1
        diameter = max(left[0]+right[0],max(left[1],right[1]))
        res.append(depth)
        res.append(diameter)
        return res
        