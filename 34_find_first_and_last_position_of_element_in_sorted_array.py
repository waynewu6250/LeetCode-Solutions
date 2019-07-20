class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        
        def bs(nums, target, if_left):
            left = 0
            right = len(nums)-1

            while left <= right:
                mid = (left+right) // 2
                if nums[mid] > target or (if_left and nums[mid]==target):
                    right = mid-1
                else:
                    left = mid+1

            return left
        
        left_idx = bs(nums, target, True)
        
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1,-1]
        else: return [left_idx, bs(nums, target, False)-1]