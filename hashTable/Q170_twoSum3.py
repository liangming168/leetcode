# -*- coding: utf-8 -*-
"""
Q170 Two Sum 3

Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example 1:

add(1); add(3); add(5);
find(4) -> true
find(7) -> false
Example 2:

add(3); add(1); add(2);
find(3) -> true
find(6) -> false
"""

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numbers = []
        

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.numbers.append(number)
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        n = len(self.numbers)
        table = {}
        for i in range(n):
            if self.numbers[i] in table:
                return True
            else:
                table[value - self.numbers[i]] = i
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)