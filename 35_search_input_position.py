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
        
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
            last = mid
        
        if nums[mid] < target:
            return mid + 1
        else:
            return mid