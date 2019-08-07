#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0
        if m == 0:
            return 0
        maximum = 0
        
        # 2d array
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    maximum = max(dp[i][j],maximum)
        
        return maximum**2
    
        # 1d array
        prev = 0
        dp = [0]*(n+1)
        for i in range(1,m+1):
            for j in range(1,n+1):
                tmp = dp[j]
                if matrix[i-1][j-1] == '1':
                    dp[j] = min(dp[j],dp[j-1],prev)+1
                    maximum = max(dp[j],maximum)
                else:
                    dp[j] = 0
                prev = tmp
        return maximum**2
