#
# @lc app=leetcode id=132 lang=python3
#
# [132] Palindrome Partitioning II
#
class Solution:
    def minCut(self, s: str) -> int:

        if not s:
            return 0
        n = len(s)
        
        dp = [0 for _ in range(n)]
        ispa = [[False]*n for _ in range(n)]
        
        for i in range(n):
            dp[i] = i
            for j in range(i+1):
                if s[i] == s[j] and (i-j <= 1 or ispa[j+1][i-1]):
                    ispa[j][i] = True
                    dp[i] = 0 if j == 0 else min(dp[j-1] + 1, dp[i])
        
        return dp[n-1]


        

