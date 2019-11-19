#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:

        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        left, right = 0, len(A)-1
        
        while left <= right:
            while left <= right and A[left] % 2 == 0:
                left += 1
            while left <= right and A[right] % 2 != 0:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        return A
        
# @lc code=end

