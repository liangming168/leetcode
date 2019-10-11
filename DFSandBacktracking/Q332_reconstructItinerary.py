# -*- coding: utf-8 -*-
"""
Q332 reconstruct itinerary

Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
"""
'''
method 1 use stack to go Euler path
initialize stack=['JFK']
curr is the top of stack, when curr is in graph and the graph[curr] is not empty 
                                just push graph[curr] first element into stack and eraes it from the graph
                          if curr is not in graph or graph[curr] is empty, add curr to the head of res
                          and pop curr out of stack

time: O(V+E), sort is VlogV, 
space: O(E)
'''
class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        
        graph = {}
        tickets.sort()
        for t in tickets:
            if t[0] not in graph:
                graph[t[0]] = []
            graph[t[0]].append(t[1])
        stack = ['JFK']   
        res = []
        print(graph)
        while stack:
            curr = stack[-1]
            if curr in graph and len(graph[curr])>0:
                stack.append(graph[curr][0])
                graph[curr].pop(0)
            else:            
                res = [curr] + res
                stack.pop()


        return res
if __name__=='__main__':
    S = Solution()
    it = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    it = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    print(S.findItinerary(it))
    
'''
DFS
'''

class Solution:
    
    def __init__(self):
        self.res = []
        
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = {}
        tickets.sort()
        for t in tickets:
            if t[0] not in graph:
                graph[t[0]] = []
            graph[t[0]].append(t[1])
        print(graph)
        self.dfs(graph,'JFK')
        return self.res

    def dfs(self,graph,curr):
        while curr in graph and len(graph[curr])>0:
            tmp = graph[curr].pop(0)
            self.dfs(graph,tmp)
        self.res = [curr] + self.res
        return
                
    
if __name__=='__main__':
    S = Solution()
    it = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    it = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    print(S.findItinerary(it))
    