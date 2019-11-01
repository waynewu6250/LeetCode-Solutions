#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums)-1
        
        while left + 1 < right:
            mid = (left+right) // 2
            if nums[right] <= nums[mid]:
                left = mid
            else:
                right = mid
        return min(nums[left], nums[right])
        
# @lc code=end

