# -*- coding: utf-8 -*-
"""
Q536 construct binary tree from string

Example:
Input: "4(2(3)(1))(6(5))"
Output: return the tree root node representing the following tree:

       4
     /   \
    2     6
   / \   / 
  3   1 5   
"""
'''
method 1 

first, find out all the node, these are the value between neigbour parenthesis

s = '('+s+')'
if encounter '(', then find till next ')' or '(', curr node is the value between the neigbour '(' and '('/")"
use a stack to store the node encounteed, if stack is not empty, the curr node should be added to the top of the stack node
if left is none, add to left otherwise right
then push curr into stack, advancing i=j

else if it's  ')' meet first, it indicates the ending of a curr, it's been used, pop it out, advancing i++
note: make sure to keep root in the stack, so when i==len(s)-1, break

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if not s:
            return None
        s = '('+s+')'
        stack = []
        i = 0
        while i<len(s):
            if s[i]== '(':
                j = i+1
                while s[j]!='(' and s[j]!=')':
                    j += 1
                curr = TreeNode(s[i+1:j]) # the curr node
                if stack: # not empty
                    if stack[-1].left is None:
                        stack[-1].left = curr
                    else:
                        stack[-1].right = curr
                stack.append(curr)
                i = j
                
            else:
                if i==len(s)-1:
                    break # make sure the root is in the stack for return
                stack.pop()
                i += 1
        return stack[-1]
    
    
                
                    