#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        answer = []
        
        for i in range(len(nums)):
            
            left = i+1
            right = len(nums)-1
            sum = -nums[i]
            
            while left < right:
                
                if nums[left] + nums[right] == sum:
                    answer.append([nums[i], nums[left], nums[right]])
                elif nums[left] + nums[right] > sum:    
                    right -= 1
                else:
                    left += 1
        
        return answer
        
# @lc code=end

