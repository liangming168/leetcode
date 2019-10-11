# -*- coding: utf-8 -*-
"""
Q91 decode ways
"""

'''
method 1 dfs backtracking
for a letter can be encoded as 1 or 2 num(s), so each time we can check 1 or 2 num(s) and then go dfs
                                                dfs(start+1) or dfs(start+2)
note: if it's a single number and it's 0, just return

time O(sqrt(3)^n), for every 2 nums pair, it could has 2 possible reuslt '12'->('1','2') or ('12'),
                                          ('1','2') call 2 dfs, ('12') call 1 dfs,  so it's 3^(n/2)
space: O(n), recursive depth
'''

class Solution:
    
    def __init__(self):
        self.res = 0
    
    def decoder(self,s):
        
        '''
        type: s string
        rtype: int
        
        '''
        if not s:
            return self.res
        self.dfs(s,0,[])
        return self.res
        
        
    def dfs(self,s, start, curr):
        if start == len(s):
            self.res += 1
            return
        tmp = chr(int(s[start:start+1]) + ord('a') - 1)
        curr.append(tmp)
        self.dfs(s,start+1,curr)
        curr.pop()
        
        if start<len(s)-1 and int(s[start:start+2])<=26:
            tmp = chr(int(s[start:start+2]) + ord('a') -1)
            curr.append(tmp)
            self.dfs(s,start+2,curr)
            curr.pop()
            
if __name__ == '__main__':
    mySolution = Solution()
    myStr = "4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"
    print(mySolution.decoder(myStr))

'''
mehtod 2 dynamic programming
for each char it can be treated as a single digit or together with its previous as 2 digits
for single digit, if it's '0' no way to decode, otherwise it has one way so it accumulate previous result
for 2 digits, if it's >=10 and <=26, it should ok and it accumlated result from pprev,otherwise no way
so every time we initiate curr = 0, if it's 0 after the check no result should be based on this decoding
so update pprev = prev, prev = curr

time: O(n)
space: O(1)
'''
class Solution:
    def decodeWays(self,s):
        
        if len(s)==0 or s[0]=='0':
            return 0
       # pprev  prev curr 
       #    1    2    3
        pprev = 1
        prev = 1
        for i in range(1,len(s)):
            curr = 0
            if s[i]=='0': #single digit
                curr += 0
            else:
                curr += prev
            if int(s[i-1:i+1])>=10 and int(s[i-1:i+1])<=26: # 2 digit
                curr += pprev
            else:
                curr += 0
            pprev = prev
            prev = curr
        
        return prev
'''
dp[i]: # of decode ways at index i
time: O(n)
space: O(n)
'''        
class Solution:
    def decodeWays(self,s):
        
        if len(s)==0 or s[0]=='0':
            return 0
       # pprev  prev curr 
       #    1    2    3

        dp = [0]*len(s)
        dp[0] = 1
        for i in range(1,len(s)):
            if s[i]!='0': #single digit
                tmp1 = dp[i-1]
            else:
                tmp1 = 0
            if int(s[i-1:i+1])>=10 and int(s[i-1:i+1])<=26: # 2 digit
                if i-2>=0:
                    tmp2 = dp[i-2]
                else:  #'12'
                    tmp2 = 1
            else:
                tmp2 = 0
            dp[i] = tmp1+tmp2 
        return dp[-1]
               