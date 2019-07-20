class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxresult = nums[0]
        maxend = nums[0]
        minend = nums[0]
        
        for i in range(1,len(nums)):
            end1 = maxend*nums[i]
            end2 = minend*nums[i]
            minend = min(min(end1,end2), nums[i])
            maxend = max(max(end1,end2), nums[i])
            maxresult = max(maxend, maxresult)
        
        return maxresult