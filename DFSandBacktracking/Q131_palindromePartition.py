# -*- coding: utf-8 -*-
"""
Q131 Palindrome Partition


"""

'''
method dfs
use dfs to iterate s from [start] to [end], if the tmp = s[start:i+1] is Palindrome,
                                            append it to the curr, then chcek the remain
                                            increae i++, dfs(s,curr,i+1)
                                            if there is other Palindrome, i increase hence [start] increase
                                            when start == len(s), it indicates the length of the Palindrome list is full
                                            otherwise [start] will never reach len(s), then for iterate go next round


time: O(n*2^n), we have 2^n combinations C(n,0)+C(n,1)+...+C(n,n), 
                for 'aaaaaa' there are 2^(n-1) partition each to put | or not in between, 
                the worst has size n, you need to traverse the entire string
space: O(2^n)
'''

class Solution:
    
    def __init__(self):
        self.res = []
    
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return self.res
        
        self.dfs(s,[],0)
        return self.res
    
    def dfs(self,s,curr,start):
        if start==len(s):
            self.res.append(curr[:])
        for i in range(start,len(s)):
            tmp = s[start:i+1]
            if tmp == tmp[::-1]:
                curr.append(tmp)
                self.dfs(s,curr,i+1)
                curr.pop()

        
if __name__ == "__main__":
    mySolution = Solution()
    print(mySolution.partition('aab'))
