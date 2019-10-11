# -*- coding: utf-8 -*-
"""
Q617 merge two binary tree

Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
 

Note: The merging process must start from the root nodes of both trees.
"""
'''
method recursion
add the result to t1
if one of the two treeNode is None, return the other
if both of them are not none, add their values
then the new tree go left with both t1 and t2 go left
                     right                       right
                     
                     
                     
time complexity: O(n), traverse all the nodes
space: O(n), worst case unbalanced O(n), in average the high of the tree is log(n),
                                         so the depth of recursion is O(logn), the stack used is O(logn)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val = t1.val + t2.val
        t1.left = self.mergeTrees(t1.left,t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1