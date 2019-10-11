# -*- coding: utf-8 -*-
"""
Q349 intersection of two arrays
Created on Thu Sep 27 21:48:10 2018

@author: Ming Liang

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Note:

Each element in the result must be unique.
The result can be in any order.
"""

'''
method 1
brute forece iterate

time complexity: O(n^2), n is max len of nums1 or nums2
space complexit: O(n) or O(1),whether consider res as extra space
'''
class Solution1:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        if not nums1 or not nums2:
            return res
        for num1 in nums1:
            if num1 in nums2 and num1 not in res:
                res.append(num1)
        return res
    
'''
method 2
sort and two pointer, hashset
first sort the two nums, then use 2 poiters to iteratre thorough, if equal add to hashset
time complexity: O(nlgn), sort use nlgn, iterate use n_min, n is the max len of nums
space complexit: O(n),the hashset
'''
class Solution2:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = set()
        if not nums1 or not nums2:
            return []
        nums1.sort() # O(mlgm)
        nums2.sort() # O(nlgn)
        p1, p2 = 0, 0
        while p1<len(nums1) and p2<len(nums2): # O(min{m,n})
            if nums1[p1] == nums2[p2]:
                res.add(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                p1 +=1
        return list(res)
    
'''
method 2
store the two list in 2 hash table
iterate through 1 hash table, then check whether the key in another hashtable

time complexity: O(2m+n), 
space complexit: O(n),
'''

class Solution3:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        if not nums1 or not nums2:
            return res
        table1 = {}
        table2 = {}
        for n1 in nums1:
            if n1 not in table1:
                table1[n1] = 1
            else:
                table1[n1] += 1
        for n2 in nums2:
            if n2 not in table2:
                table2[n2] = 1
            else:
                table2[n2] += 1
        for n1 in table1:
            if n1 in table2:
                res.append(n1)
        return res 