# -*- coding: utf-8 -*-
"""
Q206 reverse linked list

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
'''
method1
iterate 
since it's single linked list, so we first record the tmp = curr.next, it should be the new prev
exchange the direciton of the link, curr.next = prev,
then advancing the link to next, prev = curr, curr = tmp
finally, curr = None, we should use prev as head

time complextiy: O(n)
space complexity: O(1)
'''
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
   
class Solution1:
    def reverseList(self, head):

        prev = None
        curr = head
        while curr is not None:
            tmp = curr.next # store the new prev
            curr.next = prev # shift the direction of the link, point to new next
            prev = curr # advancing curr
            curr = tmp # advancing curr
        head = prev
        return head
    
'''
method2
recursive


time complextiy: O(n)
space complexity: O(n), the extra stack space, depth of the recursive function would be n, 
'''
#class ListNode:
#    def __init__(self,x):
#            head.val = x
#            head.next = None
   
class Solution2:
    def reverseList(self, head):
        return self.myReverse(head)
       
    def myReverse(self, head, prev = None):
        if not head:
            return prev
        node = head.next # advancing
        head.next = prev # reverse the direction
        return self.myReverse(node,head) # now current head is node, old head is the prev
        