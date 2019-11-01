#
# @lc app=leetcode id=852 lang=python3
#
# [852] Peak Index in a Mountain Array
#

# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:

        left = 0
        right = len(A)-1
        
        while left + 1 < right:
            mid = (left+right) // 2
            if A[mid] < A[mid+1]:
                left = mid
            else:
                right = mid
        
        return left if A[left] > A[right] else right
        
# @lc code=end

