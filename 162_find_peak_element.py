class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def recur(nums, left, right):
            if left == right:
                return left
            mid = (left+right) // 2
            if nums[mid] > nums[mid+1]:
                return recur(nums, left, mid)
            return recur(nums, mid+1, right)
            
        return recur(nums, 0, len(nums)-1)