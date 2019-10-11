# -*- coding: utf-8 -*-
"""
Q114 flatten BT into a linked lsit 

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
         
"""

'''
recursion preorder traversal

1.2.3.4.5.6 is inorder travers
6.5.4.3.2.1

go right, then left, final root, keep the track of prev node, curr node
'''

class Solution:
    def __init__(self):
        self.prev = None
        
    def flatten(self, root):
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        self.prev = root
        root.left = None