#
# @lc app=leetcode id=801 lang=python3
#
# [801] Minimum Swaps To Make Sequences Increasing
#

# @lc code=start
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:

        swaprecord = 1
        fixrecord = 0
        # everytime we should add 1 to swaprecord which means we swap; 0 to fixrecord which means we didn't swap

        for i in range(1, len(A)):
            # For this case, i-1 and i operation should be the same, otherwise it will 
            if A[i-1] >= B[i] or B[i-1] >= A[i]:
                swaprecord = swaprecord+1
                fixrecord = fixrecord
            elif A[i-1] >= A[i] or B[i-1] >= B[i]:
                tmp = swaprecord
                swaprecord = fixrecord + 1
                fixrecord = tmp
            else:
                minimum = min(swaprecord, fixrecord)
                swaprecord = minimum + 1
                fixrecord = minimum
        
        return min(swaprecord, fixrecord)
        
# @lc code=end

