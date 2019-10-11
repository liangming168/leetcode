# -*- coding: utf-8 -*-
"""
Q111 min depth of binary tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""
'''
method 1 BFS
use curr, next to store current level and next level element
if in current level, there is an element has no child, then this is the shallowest level

time: O(n)
space: O(n)
'''

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        curr = [root]
        next_ = []
        depth = 0
        while curr:
            depth += 1
            for c in curr:
                if not c.left and not c.right:
                    return depth
                if c.left:
                    next_.append(c.left)
                if c.right:
                    next_.append(c.right)

            curr = next_
            next_ = []
        return depth
    
'''
method 1 DFS
when find a leaf, it will be (0+0)+1, if one node just has only 1 child, it will be max(1,0)+1
when a node has left and right child, then choose the smaller one 

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
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left or not root.right:
            return 1+max(self.minDepth(root.left),self.minDepth(root.right))
        # or return 1+self.minDepth(root.left) + self.minDepth(root.right)
        return 1+min(self.minDepth(root.left),self.minDepth(root.right))
    