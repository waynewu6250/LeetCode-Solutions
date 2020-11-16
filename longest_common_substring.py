class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        m = len(t)
        n = len(s)
        
        # dp[i][j] represents the longest length of substring in t[:j] and s[:i]
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 0
        
        # get the maximum from dp
        max = 0
        for i in range(m+1):
            for j in range(n+1):
                if dp[i][j] > max:
                    max = dp[i][j]
        return max
