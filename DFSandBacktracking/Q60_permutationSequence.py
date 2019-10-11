# -*- coding: utf-8 -*-
"""
Q60 permutation sequence

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
"""

'''
method1 permuation all and select the Kth one

time: O(n!)
space: O(n)
'''

class Solution:
    
    def __init__(self):
        self.res = []
    
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if not n:
            return ''
        visited = [0]*(n+1)
        self.dfs(n,[],1,visited)
        return self.res[k-1]
        
    def dfs(self,n,curr,start,visited):
        
        if len(curr)==n:
            self.res.append(''.join([str(i) for i in curr[:]]))
            return
            
        for i in range(1,n+1):
            if visited[i]:
                continue
            visited[i] = 1
            curr.append(i)
            self.dfs(n,curr,start+1,visited)
            curr.pop()
            visited[i] = 0
            
'''
method1 permuation all and select the Kth one

time: O(n!)
space: O(n)
'''
'''
method2 from k calculated each digit element
[1,2,3,4,5]
the 1st is 1, then other 4 has 4! permuations
the first 2 is 1,2 then the other 3 has 3! permuations
so factorial = [1,1,2,6,24,...]
for Kth element, it's k=(k-1) index, k//factorial(i) is the first element, i from n to 0
                                    if result is 0, so it's the first element '1', etc
then update remaining k = k%factorial(i), then go to next iteration, 
            but when the element used, we don't need to use it again, pop it out, because if 
            
time: O(n)
space: O(1)
'''


class Solution:
    
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [str(i) for i in range(1,n+1)]
        factorial = [1]*n
        res = []
        for i in range(1,n):
            factorial[i] = i*factorial[i-1]
        k -= 1
        for i in range(n-1,-1,-1):
            idx = k//factorial[i]
            res.append(nums[idx])
            k = k%factorial[i]
            nums.remove(nums[idx])
        return ''.join(res)


if __name__ == '__main__':
    mySolution = Solution()
    print(mySolution.getPermutation(3,2))            