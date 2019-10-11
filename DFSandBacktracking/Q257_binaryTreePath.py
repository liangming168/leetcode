# -*- coding: utf-8 -*-
"""
Q257 binary tree path

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""

'''
method dfs

to check whether a node is leaf, if not root.left and not root.right
since, when don't check whether root is None, so when go left and right, we use if root.left, if root.right
and after each dfs since we use append to curr, we should pop curr

time: O(n), traversal every node once
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
        
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []

        self.dfs(root,[])
        return self.res
        
    def dfs(self,root,curr):
        if not root.left and not root.right:
            curr.append(str(root.val))
            self.res.append('->'.join(curr[:]))
            return
        curr.append(str(root.val))
        if root.left:
            self.dfs(root.left,curr)
            curr.pop()
        if root.right:
            self.dfs(root.right,curr)
            curr.pop()