# -*- coding: utf-8 -*-
"""
Q346 Moving Average from stream data
Created on Sun Sep 23 21:29:03 2018

@author: Ming Liang

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3 
"""
"""
method 1
use % to curricularly add/replace element in a vector in size
then sum them and divid the actually number of element     
time complexity: O(1) for next
space complexity: O(1)
"""
class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.sum = 0
        self.window = [0]*size
        self.index = -1
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.index += 1
        self.window[self.index%self.size] = val
        self.sum = sum(self.window)
        return self.sum/min(self.index+1,self.size)
        
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val) 

"""
method 1
use python build in queue:from collection import deque
deque.append(element), add element to the right of the queue
deque.popleft(), pop element from the left    
time complexity: O(1) for next
space complexity: O(1)
"""

class MovingAverage2:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size    
        self.q = collections.deque()
        self.total = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.q)==self.size:
            self.total -= self.q.popleft()
        self.q.append(val)
        self.total += val
        return self.total/len(self.q)
'''
similar as soluiton 2, use python list to achieve a queue
'''   
class MovingAverage3:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size    
        self.sum = 0
        self.q = [0]*size
        self.index = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.index += 1
        self.q.remove(self.q[0])
        self.q.append(val)
        self.sum = sum(self.q)
        return self.sum/min(self.size,self.index)
        
            
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
        
        
