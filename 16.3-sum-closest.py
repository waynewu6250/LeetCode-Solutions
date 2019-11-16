#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        
        for i in range(len(nums)):
            
            left = i+1
            right = len(nums)-1
            sum = target-nums[i]
            
            while left < right:
                
                if nums[left] + nums[right] == sum:
                    diff = 0
                if abs(diff) > abs(sum-nums[left]-nums[right]):
                    diff = sum-nums[left]-nums[right]
                if nums[left] + nums[right] > sum:    
                    right -= 1
                else:
                    left += 1
        
        return target - diff
        
# @lc code=end

