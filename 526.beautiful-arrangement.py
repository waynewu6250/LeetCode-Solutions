#
# @lc app=leetcode id=526 lang=python3
#
# [526] Beautiful Arrangement
#

# @lc code=start
class Solution:
    def countArrangement(self, N: int) -> int:

        ans = []
        items = []
        nums = list(range(1,N+1))
        visited = set()
        self.dfs(ans, items, visited, nums)
        return len(ans)
    
    def dfs(self, ans, items, visited, nums):
        
        if len(items) == len(nums):
            ans.append(items)
        
        for i in range(len(nums)):
            if nums[i] not in visited:
                if (len(items)+1) % nums[i] == 0 or nums[i] % (len(items)+1) == 0:
                    visited.add(nums[i])
                    self.dfs(ans, items+[nums[i]], visited, nums)
                    visited.remove(nums[i])
        
# @lc code=end

