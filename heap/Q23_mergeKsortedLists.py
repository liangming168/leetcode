# -*- coding: utf-8 -*-
"""
Q23 merge k sorted lists

erge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
'''
method use priority queue min heap

store the head of the k lists in a pq, every time find the smallest, use a pointer to point to the smallest node
then advancing, the point.next = tmp, point = point.next, tmp = tmp.next, pointer.next = None
if tmp is not None, push (tmp.val,tmp) into the queue

time: O(nlogk), n the total num of the elements, n = sum(ni)
space: O(k), priority queue
'''
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        myq = []
        heapq.heapify(myq)
        for i in range(len(lists)):
            if lists[i] is not None:
                heapq.heappush(myq,(lists[i].val,lists[i]))
        dummy = ListNode(-1)
        curr = dummy
        while myq:
            tmp = myq[0][1]
            curr.next = tmp
            curr = curr.next
            tmp = tmp.next
            curr.next = None
            heapq.heappop(myq)
            if tmp:
                heapq.heappush(myq,(tmp.val,tmp))
            
        return dummy.next
'''
follow-up, the k lists are vector/arrays instead of Linked list

since it's now array, we should keep track of which list and which idx of the list

time: O(nlogK)
space: O(k)
'''
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        myq = []
        heapq.heapify(myq)
        for i in range(len(lists)):
            if lists[i] is not None:
                #heapq.heappush(myq,(lists[i][idx],list_id,idx))
                heapq.heappush(myq,(lists[i][0],i,0))
        res = []
        while myq:
            tmp = myq[0]
            res.append(tmp[0])
            list_id = tmp[1]
            idx = tmp[2]
            heapq.heappop(myq)
            if idx+1<len(lists[list_id]):
                heapq.heappush(myq,(lists[list_id][idx+1],list_id,idx+1))
        return res

if __name__ == '__main__':
    myS = Solution()
    lists = [[1,2,3,50],[2,3,5],[1,3,5,7,8]]
    print(myS.mergeKLists(lists))