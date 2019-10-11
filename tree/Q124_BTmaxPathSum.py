# -*- coding: utf-8 -*-
"""
Q124 BT max path sum

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""
'''
method recursion

the max path is the sum of root.val + max(left,0) + max(right,0)
the right/left value is determined by the max of (right.right,right.left)+right.val

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
    def __init__(self):
        self.res = -float('inf')
        
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.helper(root)
        return self.res
    
    def helper(self,root):
        if not root:
            return 0
        left = max(self.helper(root.left),0)
        right = max(self.helper(root.right),0)
        self.res = max(self.res, left+right+root.val)
        return max(left,right)+root.val
'''
follow-up the the max path of it's subtree

when return ,check the max of self.res and subtree sum=right+left+root.val
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = -float('inf')
        
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.helper(root)
        return self.res
    
    def helper(self,root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        self.res = max(self.res, left+right+root.val)
        return left+right+root.val

'''
follow-up the the max path of it's sub-structure, can be subtree, sub-path or sub-node

when return ,check the max of self.res and subtree sum=right+left+root.val and sub-path = max(left,right)+root.val
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = -float('inf')
        
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.helper(root)
        return self.res
    
    def helper(self,root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        self.res = max(self.res, left+right+root.val,max(left,right)+root.val)
        return max(left+right+root.val,\
                   max(right,left)+root.val)