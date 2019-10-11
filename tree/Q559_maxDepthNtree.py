# -*- coding: utf-8 -*-
"""
Q559 max depth of n-ary tree
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example, given a 3-ary tree:
             1
          /  |  \
         2   3   4
        / \ 
       5   6
 
We should return its max depth, which is 3.

Note:

The depth of the tree is at most 1000.
The total number of nodes is at most 5000.
"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

'''
method 1 recursion
if the node is None, return 0, if the node has no child its depth is 1
then iterate all it's children, find the one with largest depth and plus 1 is the result

time: O(n)
space: O(n)
'''

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        if not root.children:
            return 1
        res = 0
        for child in root.children:
            depth_i = 1+self.maxDepth(child)
            if depth_i>res:
                res = depth_i
        return res


'''
method 1 iteration
if the node is None, return 0, if the node has no child its depth is 1
then iterate all it's children, find the one with largest depth and plus 1 is the result

time: O(n)
space: O(n)
'''

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        stack = [(1,root)]
        depth = 1
        while stack:
            curr_depth, node = stack.pop()
            depth = max(depth,curr_depth)
            for child in node.children:
                stack.append((curr_depth+1,child))
        return depth                  
