#
# @lc app=leetcode id=611 lang=python3
#
# [611] Valid Triangle Number
#

# @lc code=start
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:

        nums.sort()
        
        ans = 0
        for i in range(len(nums)):
            left, right = 0, i-1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    ans += (right-left)
                    right -= 1
                else:
                    left += 1
        return ans
        
# @lc code=end

