#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if not nums:
            return -1
        
        left = 0
        right = len(nums)-1
        
        while left + 1 < right:
            mid = (left + right) // 2
            
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid
        
        if target == nums[left]:
            return left
        if target == nums[right]:
            return right
        return -1
        
# @lc code=end

