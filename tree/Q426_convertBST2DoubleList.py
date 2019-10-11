# -*- coding: utf-8 -*-
"""
Q426 convert BST to double linked list

Convert a BST to a sorted circular doubly-linked list in-place. Think of the left 
and right pointers as synonymous to the previous and next pointers in a doubly-linked list.
"""

'''
method 1 inorder traverse recursion

use a None node as prev, inorder traverse, make the prev.right = curr, curr.left = prev, prev = curr
after that point the head.left to the end, end.right to the head

time: O(n)
space : O(h)
'''

class Node:
    def __init__(self,x,left,right):
        self.x = x
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root):
        
        if not root:
            return None
        dummy = Node(0,None,None)
        self.prev = dummy
        self.inOrder(root)
        self.prev.right = dummy.right
        dummy.right.left = self.prev
        return dummy.right
        
    
    def inOrder(self,root):
        if not root:
            return None
        self.inOrder(root.left)
        self.prev.right = root
        root.left = self.prev
        self.prev = root
        self.inOrder(root.right)
        
        
'''
method2 ietration use stack

time: O(n)
space: O(h)
'''

class Node:
    def __init__(self,x,left,right):
        self.x = x
        self.left = left
        self.right = right

class Solution2:
    def treeToDoublyList(self, root):
        if not root:
            return None
        dummy = Node(0,None,None)
        prev = dummy
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left # go left
                
            root = stack.pop()
            prev.right = root
            root.left = prev
            prev = root
            
            root = root.right # go right
            
        prev.right = dummy.right
        dummy.right.left = prev
        return dummy.right