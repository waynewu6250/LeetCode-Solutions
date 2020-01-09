#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        if not nums:
            return nums
        
        self.quicksort(nums, 0, len(nums)-1)
        return nums
        
    def quicksort(self, nums, start, end):
        
        if start >= end:
            return
        
        left = start
        right = end
        pivot = nums[(start+end)//2]
        
        while start <= end:
            while start <= end and nums[start] < pivot:
                start += 1
            while start <= end and nums[end] > pivot:
                end -= 1
            
            if start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        self.quicksort(nums, left, end)
        self.quicksort(nums, start, right)
        
# @lc code=end

