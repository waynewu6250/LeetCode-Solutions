class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        dp = [[0]*(n+1) for _ in range(n+1)]
        
        #1. recursive
        def recur(dp, l, r):
            if l >= r:
                return 0
            if dp[l][r]: return dp[l][r]
            return min(i + max(recur(dp, l, i - 1), recur(dp, i + 1, r)) for i in range(l, r + 1))
            
#         return recur(dp, 1, n)
    
        #2. iterative
        for l in range(n - 1, 0, -1):
            for r in range(l + 1, n + 1):
                dp[l][r] = min(i + max(dp[l][i - 1], dp[i + 1][r]) for i in range(l, r))
        return dp[1][n]