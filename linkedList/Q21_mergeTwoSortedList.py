# -*- coding: utf-8 -*-
"""
Q21 merge two sorted list


Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

'''
method1 iterate
use ListNode(-1) to start a head and duplicate a dummy= head to store the head for return
if l1.val<l2.val then head.next = l1 otherwise head.next = l2, then advancing head = head.next
finally return dummy.next

note: store a dummy  head for return, because the head will advancing next, next, next
      reture dummy.next to get rid of a artificial head
      
time complexity: O(n+m)
space complexity: O(1)
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        head = dummy
        while l1 and l2:
            if l1.val<l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        if l1 is not None:
            head.next = l1
        else:
            head.next = l2
        return dummy.next 

if __name__ == "__main__":
    l1 = ListNode(-1)
    dummy = l1
    for i in [1,2,4]:
        l1.next = ListNode(i)
        l1 = l1.next
    l1 = dummy.next
    
    l2 = ListNode(-1)
    dummy = l2
    for i in [1,2,3]:
        l2.next = ListNode(i)
        l2 = l2.next
    l2 = dummy.next
    mySolution = Solution()
    res = mySolution.mergeTwoLists(l1,l2)
    while res:
        print(res.val)
        res = res.next



'''
method2 recursion
if l1.val<l2.val, then we set l1.next -> add mergeTwoLists(l1.next,l2), merge the remaining l1 and l2
else, merge remaing l2 and l1
if l1 is None, then return l2, otherwise return l1
      
time complexity: O(n+m), call the merge O(m+n)time
space complexity: O(n+m), since call the recursive O(n+m) times so the stack we use will be O(m+n)
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2


if __name__ == "__main__":
    l1 = ListNode(-1)
    dummy = l1
    for i in [1,2,4]:
        l1.next = ListNode(i)
        l1 = l1.next
    l1 = dummy.next
    
    l2 = ListNode(-1)
    dummy = l2
    for i in [1,2,3]:
        l2.next = ListNode(i)
        l2 = l2.next
    l2 = dummy.next
    mySolution = Solution()
    res = mySolution.mergeTwoLists(l1,l2)
    while res:
        print(res.val)
        res = res.next