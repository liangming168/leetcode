# -*- coding: utf-8 -*-
"""
Q142 linklist cycle 2

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
"""


'''
method1 hashset

use a hashset to store the node traversed, if it appears again, then its the first

time: O(p1+2*p2), p1,p2,p3 the node before, in and after the cycle
space: O(p1+p2)
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        mySet = set()
        while head:
            if head in mySet:
                return head
            else:
                mySet.add(head)
                head = head.next
        return None
'''
method 2 two pointers

use fast, slow to check wheter there is cycle, fast goes 2 steps, slow goes 1 step
after fast = slow, reset fast at the head and fast and slow go both 1 step each time, if the meet
return fast ,this is the entry of the cycle

time: O(p1 + 2*p2 + p1)
space: O(1)
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast==slow: #there is a cycle
                fast = head
                while fast!=slow:
                    fast = fast.next
                    slow = slow.next
                return fast
        return None