# -*- coding: utf-8 -*-
"""
Q141 Linked List Cycle
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""

"""
method 1 
use a hashset to store the visited address, head= head.next, check if head in the visited 

time complexity: O(n), if there is no cycle O(n), there is cycle O(p+q), p nums pre cycle, q nums in cycle
space complexity: same as time complexity
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        visited = set()
        while head:
            if head in visited:
                return True
            else:
                visited.add(head)
            head = head.next
        return False
    
"""
method 2 two pointer
use two pointer fast and slow, each time fast goes 2 steps while slow goes 1 step
if fast==slow, there is cycle, else fast==None or fast.next== None return False
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False