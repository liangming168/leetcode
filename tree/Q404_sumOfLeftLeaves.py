# -*- coding: utf-8 -*-
"""
Q404 sum of left leaves

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""
'''
method recursion
traverse each node, if None return res
                    if not None, then if it has left  and left doesn't have children, add on left.val
then go to left and right to sum all possiblility

time: O(n), traverse every node
space: O(n), worst case unbalanced tree, in average stack used =  depth == height of tree = O(lgn)

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        res = 0
        if not root:
            return res
        if root.left and not root.left.left and not root.left.right:
            res += root.left.val
        res += self.sumOfLeftLeaves(root.left)
        res += self.sumOfLeftLeaves(root.right)
        return res
        
        