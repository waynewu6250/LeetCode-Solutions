class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        
        for i in range(2, n):
            maximum = 0
            for j in range(i-1):
                maximum = max(nums[j], maximum)
            nums[i] += maximum
            
        return max(nums)
                