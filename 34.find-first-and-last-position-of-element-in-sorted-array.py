#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        minimum = -1
        maximum = -1
        if not nums:
            return [-1, -1]
        
        left = 0
        right = len(nums)-1
        
        while left + 1 < right:
            mid = (left+right) // 2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid
        
        if target == nums[right]:
            minimum = right
        if target == nums[left]:
            minimum = left
        
        #################################
        
        left = 0
        right = len(nums)-1
        
        while left + 1 < right:
            mid = (left+right) // 2
            if target >= nums[mid]:
                left = mid
            else:
                right = mid
        
        if target == nums[left]:
            maximum = left
        if target == nums[right]:
            maximum = right
            
        return [minimum, maximum]
        
# @lc code=end

