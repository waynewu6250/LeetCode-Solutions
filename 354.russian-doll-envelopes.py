#
# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#

# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        if not envelopes:
            return 0
        
        envelopes.sort()
        n = len(envelopes)
        
        dp = [1]*n
        
        for i in range(1,n):
            for j in range(i):
                if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[j]+1, dp[i])
        
        return max(dp)

        
        
# @lc code=end

