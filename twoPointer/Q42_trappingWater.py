# -*- coding: utf-8 -*-
"""
Q42 trapping water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

'''
method two pointer

l,r pointers to keep current height, left and right to keep the left most and right most height till l,r

time: O(n)
space: O(1)
'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        left, right = 0,0 #the left and right height record
        l,r = 0, len(height)-1
        res = 0
        while l<r:
            left = max(left,height[l])
            right = max(right,height[r])
            if left<right:
                res += left-height[l]
                l += 1
            else:
                res += right - height[r]
                r -= 1
        return res
                