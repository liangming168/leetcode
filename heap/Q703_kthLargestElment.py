# -*- coding: utf-8 -*-
"""
Q703 Kth largest element in stream

Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

Example:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
Note: 
You may assume that nums' length ≥ k-1 and k ≥ 1.

@author: Ming Liang
"""

'''
method heapq, priority queue
use a priority queue to store k the raw data, and pop out smaller elements if len(nums)>k, making sure their are
only k elements in the heap such that heap[0] is the kth largest
when new elemnt comes, compare it with the top of heap, if larger replace the heap
return the top of heap

time complexity: O(logk) or O(1), build the heap nlogn, n = len(nums), for the add push is O(logk), replace is O(1)
space complexity: O(nlogn)
'''
import heapq
class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap)>k:
            heapq.heappop(self.heap)
    def add(self,val):
        if len(self.heap)<self.k:
            heapq.heappush(self.heap, val)
        elif val>self.heap[0]:
            heapq.heapreplace(self.heap,val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
if __name__ == '__main__':
    KthLargest = KthLargest(3,[3,5,6,7])
    print(KthLargest.add(7))
    print(KthLargest.add(5))
    print(KthLargest.add(7))
    