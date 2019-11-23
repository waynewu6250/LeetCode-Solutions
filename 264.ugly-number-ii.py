#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:

        heap = [1]
        visited = set([1])
        
        for i in range(n):
            val = heapq.heappop(heap)
            for factor in [2,3,5]:
                if val*factor not in visited:
                    visited.add(val*factor)
                    heapq.heappush(heap, val*factor)
        
        return val
        
# @lc code=end

