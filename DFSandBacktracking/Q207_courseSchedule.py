# -*- coding: utf-8 -*-
"""
Q207 course schedule

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
"""

'''
method dfs direct graph topological sorting

build the course as directed graph, if there is cycle, there cannot finish the course return False

topological sorting:
        1. build the directed graph
        2. use a vector to [0]*N_node, 0= unvisited, 1= visiting, 2 = visited
        3.dfs, if v[i] = 1: return has cycle, v[i] =2 , already visited, 
          mark it as v[i] = 1, go check it's neigbour, if it's neigbour has cycle, then return has cylce
          else, no cycle, mark is as visited v[i]=2, return 
          
time: O(n), visited each node only once
space: O(n)
          
'''
class Solution:
    
    def canFinish(self, numCourses, pre):
        if not numCourses:
            return True
        if not pre:
            return True
        
        graph = [[] for _ in range(numCourses)] # don' use [[]*numCousrses] == [[]]
        for p in pre:
            graph[p[0]].append(p[1])
        # 0= unvisited, 1= visiting, 2= visited
        status = [0]*numCourses
        for i in range(numCourses):
            if self.dfs(i,status,graph): # if has cycle
                return False
        return True
    
    def dfs(self,i,status,graph):
        # topological sorting
        if status[i] == 2:
            return False
        if status[i] == 1:  # always visting, has a cycle
            return True
        status[i] = 1
        for node in graph[i]:
            if self.dfs(node,status,graph):
                return True
        status[i] = 2
        return False
        