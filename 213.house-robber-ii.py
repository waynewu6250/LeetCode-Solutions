#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        def max_rob(numm):
            for i in range(2,len(numm)):
                maxnum = 0
                for j in range(i-1):
                    maxnum = max(numm[j],maxnum)
                numm[i] += maxnum
            return max(numm)
        
        return max(max_rob(nums[:-1]), max_rob(nums[1:]))

