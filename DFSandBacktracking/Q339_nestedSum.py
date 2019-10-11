# -*- coding: utf-8 -*-
"""
Q339 nested sum
Created on Sun Sep 23 21:29:03 2018

@author: Ming Liang


Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: 10 
Explanation: Four 1's at depth 2, one 2 at depth 1.
"""
"""
method
use dfs
iterate the nestedList,
if the element is int, then add on with depth
else go to next layer dfs with depth++

note:(1) when is not int, res = res + next_dfs
     (2) set res=0 at the beginning of the dfs function, because we just need to add integer value, the res
     is accumulated by (1)
     
time complexity: O(n)
space complexity: O(1)
"""

class Solution:
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """

        k = 1
        res = self.dfs(k,nestedList)
        return res
    
    def dfs(self,k,nestedList):
        res = 0
        for element in nestedList:
            if isinstance(element,int):
                res += element*k
            else:
                res += self.dfs(k+1,element)
        return res
        
if __name__ == "__main__":
    mySolution = Solution()
    print(mySolution.depthSum([[1,1],2,[1,1]]))
        
        
        
        
        