class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        n = len(nums)
        dp = [0]*n
        dp[0] = 1
        
        for i in range(1,n):
            maximum = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    maximum = max(dp[j],maximum)
                    dp[i] = maximum
            dp[i] += 1
                
        return max(dp)