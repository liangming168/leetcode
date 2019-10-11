# -*- coding: utf-8 -*-
"""
Q322 coin change

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
"""

'''
method DP

dp[i]: the fewest number of coins for amount i

dp[i] = min(dp[i-coins[j]]+1,dp[i])

time: O(m*n), m the amount, n coins value
space: O(m), dp array
'''

class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for i in range(1,len(dp)):
            for j in range(len(coins)):
                if coins[j]<=i:
                    dp[i] = min(dp[i-coins[j]]+1,dp[i])
        if dp[-1]>amount:
            return -1
        return dp[-1] 
    
if __name__=='__main__':
    S = Solution()
    print(S.coinChange([370,417,408,156,143,434,168,83,177,280,117],9953))
        