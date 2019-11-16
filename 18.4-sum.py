#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        answer = []
        
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1,len(nums)-2):
                if j != i+1 and nums[j] == nums[j-1]:
                    continue
                
                new_target = target - nums[i] - nums[j]
                left = j+1
                right = len(nums)-1
                while left < right:
                    if nums[left]+nums[right] == new_target:
                        answer.append([nums[i], nums[j], nums[left], nums[right]])
                        right -= 1
                        left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                    elif nums[left]+nums[right] > new_target:
                        right -= 1
                    else:
                        left += 1
                
        return answer

        
# @lc code=end

