#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        left = 0
        right = 0
        maxlen = 0
        while right < len(nums):
            if nums[right] == 0:
                maxlen = max(right-left, maxlen)
                right += 1
                left = right
            else:
                right += 1
        
        maxlen = max(right-left, maxlen)
        return maxlen
        
# @lc code=end

