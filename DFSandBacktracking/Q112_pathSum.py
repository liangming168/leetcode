# -*- coding: utf-8 -*-
"""
Q112 path sum
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""
'''
method dfs

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
    def __init__(self):
        self.res = []
        
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        self.dfs(root,[])
        if sum in self.res:
            return True
        else:
            return False
        
    def dfs(self,root,curr):
        if not root.left and not root.right:
            curr.append(root.val)
            self.res.append(sum(curr))
            return
        curr.append(root.val)
        if root.left:
            self.dfs(root.left,curr)
            curr.pop()
        if root.right:
            self.dfs(root.right,curr)
            curr.pop()
        