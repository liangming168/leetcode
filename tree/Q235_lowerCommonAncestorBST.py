# -*- coding: utf-8 -*-
"""
Q234=5 lower common ancestor of BST

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself 
             according to the LCA definition.
Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.
"""


'''
method 1 recursion bottom-up

if find p or q return root, 
divide to left and right
conquer if find result in left and right, i.e. left is not None and right is not None return the root
if left is None, it should at the right side
if rifht is None, it should at the left

time: O(n)
space; O(n)
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root==p or root==q:
            return root

        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        
        if left and right: #if left and right both have not None return
            return root
        if not left:
            return right
        if not right:
            return left
        
'''
mehtod 2 iterate top-down
since it's BST, the left is smaller than the root, right is larger than root

time: O(n)
space: O(1)
'''
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        while root:
            if root.val>max(p.val, q.val):
                root = root.left
            elif root.val<min(p.val, q.val):
                root = root.right
            else:
                return root
            
            
'''
mehtod 2 recursion 
since it's BST, the left is smaller than the root, right is larger than root

time: O(n)
space: O(n)
'''
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if min(p.val,q.val)>root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        elif max(p.val,q.val)<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return root