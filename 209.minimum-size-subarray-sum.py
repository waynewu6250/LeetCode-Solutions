#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:

        left = 0
        sum = 0
        ans = float('inf')
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= s:
                ans = min(ans, i-left+1)
                sum -= nums[left]
                left += 1
        return ans if ans != float('inf') else 0
        
# @lc code=end

