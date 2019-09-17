#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change 2
#
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        # 1. combination sum
#         answer = []
#         items = []
        
#         def recur(items, start, target):
            
#             if target == 0:
#                 answer.append(items)
#                 return
            
#             if target < 0:
#                 return
            
#             for i in range(start, len(coins)):
#                 recur(items+[coins[i]], i, target-coins[i])
            
#         recur(items, 0, amount)
#         return len(answer)
        
        # 2. dp
        if amount == 0 and coins is None:
            return 1
        dp = [0] * (amount + 1)
        dp[0] = 1 
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]
        

