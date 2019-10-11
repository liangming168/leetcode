# -*- coding: utf-8 -*-
"""
Q47 permutaion 2

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
'''
method dfs backtracking

compared with permutaion I, we need to avoid duplicated permutations
we use visied[i] to avoid revisit a element in the same recursion depth in permutaion I
but if there is duplicated elements, we need to check num[i] == num [i-1] and visited[i-1] ==1,
                                                    meaning the same number has been visited already
note: to make sure same elements are neigbours, we need to sort nums                                                    

time: O(n!)
space: O(n)
'''

class Solution:
    
    def __init__(self):
        self.res = []
        
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<=1:
            return [nums]
        curr = []
        visited = [0] *len(nums)
        nums.sort()
        self.backtracking(curr,nums,visited)
        return self.res
    
    def backtracking(self,curr,nums,visited):
        print(curr[:])
        if len(curr) == len(nums):
            self.res.append(curr[:])
            return
        
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1] and visited[i-1]==1:
                continue
            if visited[i]:
                continue
                
            visited[i] = 1
            print('**',visited)
            curr.append(nums[i])
            self.backtracking(curr,nums,visited)
            visited[i] = 0
            curr.pop()
            print('***',visited)

if __name__ == '__main__':
    mySolution = Solution()
    print(mySolution.permuteUnique([1,1,2]))