class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        target = 0
        
        def swap(nums, a, b):
            tmp = nums[a]
            nums[a] = nums[b]
            nums[b] = tmp
            return nums
        
        # Find the first small element
        for i in range(len(nums)-1,-1,-1):
            if nums[i] > nums[i-1]:
                target = i-1
                break
        
        # Find first element larger than target
        if target >= 0:
            for i in range(len(nums)-1,-1,-1):
                if nums[i] > nums[target]:
                    nums = swap(nums, i, target)
                    break
                    
        # Reverse elements larger than target
        left = target+1
        right = len(nums)-1
        
        while left < right:
            nums = swap(nums,left,right)
            left += 1
            right -= 1