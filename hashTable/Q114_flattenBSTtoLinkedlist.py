# -*- coding: utf-8 -*-
"""
Q114 flatten binary tree to linked list
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
method dfs
we can go dfs to the right first then left,
we root is None return, then we can traverse 6->5->4->3->2->1
then we can build a linked list from tail to head

Note: set the head of the linked list as none, self.prev = None
'''
#class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
#
#class LinkedList:
#    def __init__(self,x):
#        self.val = x
#        self.prev = None

class Solution:
    def __init__(self):
        self.prev = None
    def flatten(self, root):
        '''
        type: TreeNode
        rtype: void, in place the tree to a linked list
        '''
        if not root:
            return None
        
        self.flatten(root.right)
        self.flatten(root.left)
        
        root.right = self.prev
        self.prev = root
        root.right = None
