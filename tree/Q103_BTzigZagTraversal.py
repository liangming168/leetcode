# -*- coding: utf-8 -*-
"""
Q103 BT zigzag level order traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

'''
method BFS

use curr and next to record curr layer and it's children, then append each layers to res,
if odd layer prime sequence, otherwise reversely.

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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        curr = [root]
        next_ = []
        res = []
        flag = 1
        while curr:
            tmp = []
            for node in curr:
                if flag%2 == 1:
                    tmp.append(node.val)
                else:
                    tmp = [node.val] + tmp
                if node.left:
                    next_.append(node.left)
                if node.right:
                    next_.append(node.right)
            '''
            if flag%2 == 1:
                res.append(tmp)
            else:
                res.append(tmp[::-1])
            '''
            res.append(tmp)
            flag += 1
            curr = next_
            next_ = []
        
        return res
                
        