# -*- coding: utf-8 -*-
"""
Q144 binary tree preoder traversal

Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
'''
method 1 recusion
if not root, return []
then first root come, append to res, then go left, then right

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
        
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.res.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return self.res
    
'''
method 1 iteration
use a stack to store current node, then pop out the node and add it's value to result, then go next level 
and push it's children to the stack

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right) # since stack is first in last out
                stack.append(node.left) # push right side in first, to pop out later than left
        return res