# -*- coding: utf-8 -*-
"""
Q107 binary tree level order traversal 2

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""

'''
method 1 DFS
need to find the height of the tree, then reverse upside down

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
    def __init__(self):
        self.res = []
        
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        h = self.findHeight(root)
        while h:
            self.res.append([])
            h -= 1

        self.dfs(root,0,h-1)
        return self.res
    
    def dfs(self,root,h,height):
        if not root:
            return
        
        self.res[height-h].append(root.val)
        self.dfs(root.left,h+1,height)
        self.dfs(root.right,h+1,height)
        
        
    def findHeight(self,root):
        if not root:
            return 0
        L = self.findHeight(root.left)
        R = self.findHeight(root.right)
        if L>R:
            return L+1
        else:
            return R+1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


'''
method 2 BFS
every time, when a new level got, add to the head of the res

note: when add lsit to list of list, use extra [list]
      e.g. a = [[1],[1],[1]], b=[3], a = [b] + a = [[3],[1],[1],[1]]
                                 if  a = b + a = [3,[1],[1],[1]]

time: O(n)
space: O(n)
'''
class Solution:

        
    def levelOrderBottom(self, root):
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
            tmp = []
            for element in curr:
                tmp.append(element.val)
                if element.left:
                    next_.append(element.left)
                if element.right:
                    next_.append(element.right)
            res = [tmp] + res
            curr = next_
            next_ = []
            
        return res