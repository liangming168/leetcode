# -*- coding: utf-8 -*-
"""
Q350 intersection of two arrays II
Created on Thu Sep 27 21:48:10 2018

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""


'''
method 
sort and two pointer, 
first sort the two nums, then use 2 poiters to iteratre thorough, if equal add to list
time complexity: O(nlgn), sort use nlgn, iterate use n_min, n is the max len of nums
space complexit: O(n),the list
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
        return res
    
'''
method 2
store the two list in 2 hash table, and cnt the numsber value
iterate through 1 hash table, then check whether the key in another hashtable

time complexity: O(2m+n), 
space complexit: O(m+n),
'''
class Solution2:
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
        for n1 in nums1:  # O(m)
            if n1 not in table1:
                table1[n1] = 1
            else:
                table1[n1] += 1
        for n2 in nums2: # O(n)
            if n2 not in table2:
                table2[n2] = 1
            else:
                table2[n2] += 1
        for n1 in table1:  # {O(m)  /  O(1) } = O(m)
            if n1 in table2: # O(1)
                k = min(table1[n1],table2[n1])  
                while k:  # O(1)  /  O(m)
                    res.append(n1)
                    k -= 1
        return res 
    
'''
method 2
if nums2 is very large and store in hard disk,
so just build 1 table for num1, and read in nums2 in chunks

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

        for n1 in nums1:  # O(m)
            if n1 not in table1:
                table1[n1] = 1
            else:
                table1[n1] += 1
   
        for data in nums2:
            if data in table1 and table1[data]>0: 
                res.append(data)
                table1[data] -= 1
        return res 
        