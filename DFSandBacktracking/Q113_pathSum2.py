# -*- coding: utf-8 -*-
"""
Q113 path sum 2

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
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
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.dfs(root,[],sum)
        return self.res
        
    def dfs(self,root,curr,target):
        if not root.left and not root.right:
            curr.append(root.val)
            if sum(curr)==target:
                self.res.append(curr[:])
            return 
        curr.append(root.val)
        if root.left:
            self.dfs(root.left,curr,target)
            curr.pop()
        if root.right:
            self.dfs(root.right,curr,target)
            curr.pop()