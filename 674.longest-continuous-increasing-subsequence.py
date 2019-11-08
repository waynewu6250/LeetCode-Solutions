#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        left = 0
        right = 1
        maxlen = 0
        while right <= len(nums):
            if right == len(nums) or nums[right] <= nums[right-1]:
                maxlen = max(right-left, maxlen)
                left = right
            right += 1
        
        
        return maxlen
        
# @lc code=end

