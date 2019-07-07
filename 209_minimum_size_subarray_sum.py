class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        sum = 0
        ans = float('inf')
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= s:
                ans = min(ans, i-left+1)
                sum -= nums[left]
                left += 1
        return ans if ans != float('inf') else 0