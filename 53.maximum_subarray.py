class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #1. 
        for i in range(1,len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
    
        #2.
        cursum = nums[0]
        maxsum = cursum
        for i in range(1,len(nums)):
            if cursum > 0:
                cursum += nums[i]
            else:
                cursum = nums[i]
            maxsum = max(cursum, maxsum)
        return maxsum