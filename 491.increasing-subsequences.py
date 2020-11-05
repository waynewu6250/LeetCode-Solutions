#
# @lc app=leetcode id=491 lang=python3
#
# [491] Increasing Subsequences
#

# @lc code=start
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        ans = []
        items = []
        self.dfs(ans, items, 0, nums, set())
        return ans
    
    def dfs(self, ans, items, start, nums, visited):
        
        if len(items) >= 2 and tuple(items) not in visited:
            visited.add(tuple(items))
            ans.append(items)
        
        for i in range(start, len(nums)):
            if len(items) < 1:
                self.dfs(ans, items+[nums[i]], i+1, nums, visited)
            elif len(items) >= 1 and items[-1] <= nums[i]:
                self.dfs(ans, items+[nums[i]], i+1, nums, visited)
        
# @lc code=end

