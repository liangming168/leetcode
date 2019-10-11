# -*- coding: utf-8 -*-
"""
Q143 reorder list

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""

'''
method the first half sequence inorder, the second half reverse the order
1. find the middle node
2. reverse the second half
3. merge the two list
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        # find the middle node
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        head2 = slow.next
        slow.next = None # the first list from head to slow
        
        #reverse the second list
        head2 = self.reverseList(head2)
        
        #merge list
        head1 = head
        while head2:
            tmp1 = head1.next
            tmp2 = head2.next
            head1.next = head2
            head2.next = tmp1
            head1 = tmp1
            head2 = tmp2
    
    def reverseList(self,head):
        if not head or not head.next:
            return head
        prev = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        head = prev
        return head