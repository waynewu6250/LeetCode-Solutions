class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0]*(amount+1)
        
        for i in range(1,amount+1):
            minimum = float('inf')
            
            for j in coins:
                if i-j >= 0:
                    minimum = min(dp[i-j]+1, minimum)
            dp[i] = minimum
        
        return dp[-1] if dp[-1] != float('inf') else -1