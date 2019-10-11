# -*- coding: utf-8 -*-
"""
Q157 Read N characters given read4
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file to buf.

Example 1:

Input: buf = "abc", n = 4
Output: 3 
Explanation: The actual number of characters read is 3, which is "abc".
Example 2:

Input: buf = "abcde", n = 5 
Output: 5
Note:
The read function will only be called once for each test case.
"""


# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        idx = 0

        while n:
            # read file into buf4
            buf4 = ['FB']*4
            l = read4(buf4)
            if not l:
                return idx
            #write buf4 to buf
            for i in range(min(l,n)): # in case n is smaller than l
                buf[idx] = buf4[i]
                idx += 1
                n -= 1
        return idx