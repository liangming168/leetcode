# -*- coding: utf-8 -*-
"""
Q6 zig zag conversation
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""

'''
method 1
use a list of ['']*numRows to store the element in each row, row = 0 to start
iterate all the letters in s, if flag = 0, row++, else row--
if row>numRows, row-2, and change from increase to decrease, i.e. flag=1
if row<0, row+2, change to increase row, flag=0

time complexity: O(n)
space comlexity: O(n)

'''

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <=1:
            return s
        res = [''] * numRows
        result = ''
        flag = 0 # if 0 ,row increase; 1, row decrease
        row = 0
        for element in s:
            res[row] += element
            
            if flag == 0:
                row += 1
            else:
                row -= 1
                
            if row >= numRows:
                flag = 1
                row -= 2
            if row < 0:
                flag = 0
                row += 2

        for r in res:
            result += r
            
        return result
            
        
        