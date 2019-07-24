class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)
        
        for i in range(1,n+1):
            minimum = float('inf')
            j = 1
            while j*j <= i:
                # + 1 means I use up this number j*j
                minimum = min(dp[i-j*j]+1,minimum)
                j += 1
            dp[i] = minimum
        return dp[n]