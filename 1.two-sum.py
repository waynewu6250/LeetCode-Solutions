#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # front-back
        # nums = sorted(nums)
        # left = 0
        # right = len(nums)-1
        
        # while left < right:
        #     if nums[left]+nums[right] > target:
        #         right-=1
        #     elif nums[left]+nums[right] < target:
        #         left+=1
        #     else:
        #         return [left, right]


        # minus
        
        # hashtable
        dic = {num: i for i, num in enumerate(nums)}
        
        for i, num in enumerate(nums):
            if (target-num) in dic and i != dic[target-num]:
                return [i, dic[target-num]]

        

