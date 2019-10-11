# -*- coding: utf-8 -*-
"""
Q110 balanced binary tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""
'''
method 1 recursion from top-down

check each node whether its left and right is balanced, and the height of right and left <=1

time: O(n^2), isbalacne recursively traverse all the node once O(n), for height the worst case is O(n), so O(n^2)
space: space(n)  
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return True
        if abs(self.height(root.left)-self.height(root.right))<=1\
        and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False
    def height(self,root):
        if not root:
            return 0
        return 1+max(self.height(root.left),self.height(root.right))
    
    
    
'''
method 2 recursion bottom-up

for the none node reutrn 0, then like find the depth traversal, return 1+max(left,right)
but when abs(left-right)>1 we return a False then we add this False to the upper height, 
                            that is, if one of left/right is False, return False
note: since right/left can be a number or False, to check whether is False, use if right is False
                                                                    istead of use if not right, in case right=0

time: O(n), 
space: space(n)  
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if self.helper(root):
            return True
        else:
            return False
    def helper(self,root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        if (left is False) or (right is False) or abs(left-right)>1:
            return False
        else:
            return 1+max(left,right)
        
'''
method 3 use stack to iterate

time: O(n)
space: O(n)
'''       
class Solution(object):
    def isBalanced(self, root):
        stack, node, last, depths = [], root, None, {}
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    node = stack.pop()
                    left, right  = depths.get(node.left, 0), depths.get(node.right, 0)
                    if abs(left - right) > 1: return False
                    depths[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right
        return True