# -*- coding: utf-8 -*-
"""


Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"] 
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []
Created on Fri Nov  9 18:14:55 2018

@author: Ming Liang
"""

class Solution1:
    def __init__(self):
        self.res = []
    
    def addOperators(self,s,target):
        if not s:
            return []
        for i in range(len(s)):
            if i>0 and s[0]=='0':
                break
            curr = s[0:i+1]
            currval = int(curr)
            self.dfs(s,target,curr,currval,currval,i+1,'+')
        return self.res
    
    def dfs(self,s,target,curr,currval,preval,i,op):
        if i==len(s):
            if target == currval:
                self.res.append(curr)
            return 
        for j in range(i,len(s)):
            if j>i and s[i]=='0':
                return 
            tmp = s[i:j+1]
            tmpval = int(tmp)
            self.dfs(s,target,curr+'+'+tmp,currval+tmpval,tmpval,j+1,'+')
            self.dfs(s,target,curr+'-'+tmp,currval-tmpval,tmpval,j+1,'-')
            if op=='+': # 1+1*1
                self.dfs(s,target,curr+'*'+tmp,currval-preval+preval*tmpval,preval*tmpval,j+1,op)
            if op=='-': # 1-1*1
                self.dfs(s,target,curr+'*'+tmp,currval+preval-preval*tmpval,preval*tmpval,j+1,op)

if __name__=='__main__':
    s = "232"
    target = 8
    obj = Solution1()
    print(obj.addOperators(s,target))
    print('***')
'''
simple verison, only '+' and  '-' 
'''

class Solution2:
    def __init__(self):
        self.res = []
        
    def addOperators(self,s,target):
        for i in range(len(s)):
            if i>0 and s[0]=='0': # avoid begining 0: '01','00'
                break
            curr = s[0:i+1]
            currval = int(curr)
            self.dfs(s,target,curr,currval,i+1)
           
        return self.res
    
    def dfs(self,s,target,curr,currval,i):
        if i==len(s):
            if currval==target:
                self.res.append(curr)
            return
        
        for j in range(i,len(s)):
            if j>i and s[i]=='0':
                return
            tmp = s[i:j+1]
            tmpval = int(tmp)
            self.dfs(s,target,curr+'+'+tmp,currval+tmpval,j+1)
            self.dfs(s,target,curr+'-'+tmp,currval-tmpval,j+1)
            
if __name__ == '__main__':
    target = 100
    s = '10101'
    target = 5
    s= '105'
    obj = Solution2()
    print(obj.addOperators(s,target))