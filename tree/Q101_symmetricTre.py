# -*- coding: utf-8 -*-
"""
Q101 symmetric tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
"""
'''
method 1 recursion
if symmetric, left and right subtree should be symmetric, and left tree and right tree should miror each other

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
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.helper(root.left,root.right)
    
    def helper(self,left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.helper(left.left,right.right) and\
                                self.helper(left.right,right.left)
'''
method 2 iterata use stack

left in first, right in second, so right out first, 
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack = []
        stack.append(root.left)
        stack.append(root.right)
        while stack:
            right = stack.pop()
            left = stack.pop()
            if not right and not left:
                continue
            if not right or not left or left.val != right.val:
                return False
            stack.append(left.left)
            stack.append(right.right)
            stack.append(right.left)
            stack.append(left.right)
        return True