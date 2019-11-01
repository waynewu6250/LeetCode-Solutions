#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left = 1
        right = max(piles)
        
        while left + 1 < right:
            mid = (left+right) // 2
            if self.hours_to_eat(piles, mid) <= H:
                right = mid
            else:
                left = mid
        
        minimum = float('inf')
        if self.hours_to_eat(piles, left) <= H:
            minimum = left
        if self.hours_to_eat(piles, right) <= H:
            minimum = min(minimum, right)
        
        
        return minimum
        
    
    def hours_to_eat(self, piles, K):
        hours = 0
        for pile in piles:
            eat = pile // K if pile % K == 0 else pile // K+1
            hours += eat
        return hours
        
# @lc code=end

