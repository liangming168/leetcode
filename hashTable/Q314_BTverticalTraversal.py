# -*- coding: utf-8 -*-
"""
Q314 binary tree vertical order traversal

Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples 1:

Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7 

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]
Examples 2:

Input: [3,9,8,4,0,1,7]

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7 

Output:

[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Examples 3:

Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2

Output:

[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]
"""

'''
method hashtable

use a hashtable to record the col number and add corresponding node val to its col
then use a que to store current node and it's col, if there is no key of the col, add key and then add val to corresponding key
after que is empty, done
for the result, iterate the table for all the col, and add to the result

time: O(n)
space: O(n)
'''
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Soltuion:
    def BTverticalTraversal(self,root):
        if not root:
            return []
        table = {}# record col and corresponding node val
        que =[(root,0)]
        minCol, maxCol = float('inf'), -float('inf')
        while que:
            f = que.pop(0)
            node = f[0]
            col = f[1]
            if col not in table:
                table[col] = []
            table[col].append(node.val)
            minCol = min(col, minCol)
            maxCol = max(col, maxCol)
            if node.left:
                que.append((node.left,col-1))
            if node.right:
                que.append(node.right,col+1)
        res = []
        for i in range(minCol, maxCol + 1):
            res.append(table[i])
        return res
            