# -*- coding: utf-8 -*-
"""
Q210 course schdedule 2

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another 
"""

'''
method graph topological sorting
same as course schedule 1
just add the course to the result when it's been visited

time: O(n)
space: O(n)
'''

class Solution:
    def __init__(self):
        self.res = []
        
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if not numCourses:
            return []
        if not prerequisites:
            return [i for i in range(numCourses)]
        graph = [[] for _ in range(numCourses)]
        for p in prerequisites:
            graph[p[0]].append(p[1])
        # 0=unvisied, 1= visiting, 2=visited
        status = [0]*numCourses
        for i in range(numCourses):
            if self.dfs(i,status,graph): # there is cycle
                return []
        return self.res
    
    def dfs(self,i,status,graph):
        if status[i] == 2:
            return False
        if status[i] == 1: # always visiting, there is cycle
            return True
        status[i] = 1
        for node in graph[i]:
            if self.dfs(node,status,graph):
                return True # there is cycle
        status[i] = 2
        self.res.append(i)
        return False # no cycle