#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if len(intervals) == 0:
            return 0
        
        # 1. dp
        # intervals = sorted(intervals, key = lambda x: x[0])
#         n = len(intervals)
#         dp = [0]*n
#         dp[0] = 1
        
#         for i in range(1,n):
#             maximum = 0
#             for j in range(i):
#                 if intervals[j][1] <= intervals[i][0]:
#                     maximum = max(dp[j],maximum)
#             dp[i] = maximum+1
#         print(dp)
#         return n-max(dp)
    
        # 2. greedy
        intervals = sorted(intervals, key = lambda x: x[1])
        print(intervals)
        min_remv = 0
        min_end = -float('inf')
        for interval in intervals:
            if interval[0] < min_end:
                min_remv += 1
            else:
                min_end = interval[1]
        return min_remv
        

