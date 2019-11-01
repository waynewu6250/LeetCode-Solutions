class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #1. add and sort
        #2. run nums and find position directly (O(N))
        #3. binary search (O(logN))
        
        # method 1: search range
        left = 0
        right = len(nums)-1
        
        while left + 1 < right:
            mid = (left+right) // 2
            if target >= nums[mid]:
                left = mid
            else:
                right = mid
        
        if target <= nums[left]:
            return left
        if target <= nums[right]:
            return right
        
        return right+1

        # method 2: find directly
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = (left+right) // 2
            if target <= nums[mid]:
                right = mid-1
            else:
                left = mid+1
        return left
