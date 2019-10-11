# -*- coding: utf-8 -*-
"""
Q98 validate BST

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
"""

'''
method 1 recursion

check whether the node val is within reasonable range
if go left subtree, update the uppper bound as the curr node val
if go right subtree, update the lower bound as the curr node val

time: O(n)
space: O(h)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root or (not root.left and not root.right):
            return True
        return self.helper(root,-float('inf'),float('inf'))
        
    def helper(self,root,currMin, currMax):
        if not root:
            return True
        
        if root.val<= currMin or root.val>=currMax:
            return False
        return self.helper(root.left,currMin, root.val) and self.helper(root.right,root.val,currMax)
    
'''
method2 inorder traverse, store the result in a list, in the list is increasing it's true
                                   no need to store the whole list, just previous value is enough
'''    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.prev = -float('inf')

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root or (not root.left and not root.right):
            return True
        
        return self.inOrder(root)
        
        
    def inOrder(self,root):
        if not root:
            return True

        if not self.inOrder(root.left):
            return False
        if root.val<=self.prev:
            return False
        self.prev = root.val
        return self.inOrder(root.right)
        
