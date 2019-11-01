#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:

        # There is no method with complexity < O(n), since in the worst case, 1111101111, you should definitely look up every 1 in order to find 0.
        
        minimum = float('inf')
        for i in range(len(nums)):
            minimum = min(nums[i], minimum)
        return minimum

        
# @lc code=end

