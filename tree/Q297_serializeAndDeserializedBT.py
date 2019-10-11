# -*- coding: utf-8 -*-
"""
Q297 serialize and deserialize a binary tree

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
"""

'''
method 1 recursion
serialize: preorder traverse the tree, if node is node mark as '#', return the preorder result in string
deserialize: preorder traverse, if '#' return None, else build a treeNode,treeNode.left call the sub function 
                                                    then treeNode.right call the subfunction
                                                    
time: O(n)
space: O(n)
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#'
        res = self.preOrder(root,[])
        return ' '.join(res)# blank to seperate
        
    def preOrder(self,root,res):
        if not root:
            res.append('#')
            return 
        res.append(str(root.val))
        self.preOrder(root.left,res)
        self.preOrder(root.right,res)
        return res
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(' ')
        root = self.helper(vals)
        return root
        
    def helper(self,vals):
        while vals:
            curr = vals.pop(0)
            if curr == '#':
                return None
            node = TreeNode(int(curr))
            node.left = self.helper(vals)
            node.right = self.helper(vals)
            return node

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
