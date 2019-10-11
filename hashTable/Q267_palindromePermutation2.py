# -*- coding: utf-8 -*-
"""
Q267 Palindrome Permutation II
Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

Example 1:

Input: "aabb"
Output: ["abba", "baab"]
Example 2:

Input: "abc"
Output: []
a=[1,2,3,]
"""
'''
method backtracking
use hashset to store the char, if not char not in hashset, add in ,else remove
use list to store the char that has duplicates

after done,there is 1 or 0 element in hashset, it's palindrome
then if len(hashset) ==1, the only one element should be in the mid of the parlindrome
                             otherwise, the mid=''

then use backtracking to generate palindrome list, we just need generate one half

time complexity: O((n/2)!), because for the backtracking is n/2*(n-1)/2*(n-2)/2....
space complexity: O(n), for hashset and list O(n), for backtracking depth is n/2, so space O(n/2)
'''


class Solution:
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s)==1:
            return [s]
        charSet = set()
        charList = []
        
        for i in sorted(s):
            if i in charSet:
                charSet.remove(i)
                charList.append(i)
            else:
                charSet.add(i)
                
        if len(charSet)>1:
            return []
        
        if len(charSet)==1:
            mid = list(charSet)[0]
        else:
            mid = ''

        visited = [0]*len(charList)
        outList = []
        curr = ''
        self.backTracking(visited, mid, outList,charList,curr)
        return outList
    
    def backTracking(self,visited, mid, outList,charList,curr):
        if len(curr) == len(charList):
            outList.append(curr + mid + curr[::-1])
            return
        for i in range(len(charList)):
            if i > 0 and visited[i-1] == 0 and charList[i] == charList[i-1]: continue
            if visited[i] ==0:
                visited[i] = 1
                self.backTracking(visited,mid,outList,charList,curr+charList[i])
                visited[i] = 0
                
if __name__ == '__main__':
    mySolution = Solution()
    print(mySolution.generatePalindromes('abbbb'))