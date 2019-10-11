# -*- coding: utf-8 -*-
"""
Q102 binary tree level order traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

'''
method 1 BFS
iterate from height 0 to h
use curr and next to store nodes in current and next level/height
to find next nodes, iterate all current nodes and add its left and right to next, if any
                                at the same time, add the curr node val to curr level sublist
if curr[node] is empty stop


====================================================
the method to find the depth of a binary search tree, return would be N levels, from 0 to N-1,
                                                                                height is N-1

def dfs(self,root):
    if not root:
        return 0
    
    L = self.dfs(root.left)
    R = self.dfs(root.right)
    if L>R:
        return L+1
    else:
        return R+1
=====================================================
time: O(n), traverse each node once
space: O(n), worst case 1 height
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        curr = [root]
        next_ = []
        res = []
        while curr:
            level = []
            for c in curr:
                level.append(c.val)
                if c.left:
                    next_.append(c.left)
                if c.right:
                    next_.append(c.right)
            res.append(level)
            curr = next_
            next_ = []
        return res
    
    

'''
method 1 DFS
add empty [] to the result, from height 0 to height h, if there is node, at node.val for sublist in this level 
                               res[h].append(root.val)

time: O(n), traverse each node once
space: O(n), worst case 1 height
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def __init__(self):
        self.res = []
        
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        self.dfs(root,0)
        return self.res
    
    
    def dfs(self,root,h):
        if not root:
            return
        while len(self.res)<=h:
            self.res.append([])
        self.res[h].append(root.val)
        self.dfs(root.left,h+1)
        self.dfs(root.right,h+1)
        
            