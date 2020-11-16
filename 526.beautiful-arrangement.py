#
# @lc app=leetcode id=526 lang=python3
#
# [526] Beautiful Arrangement
#

# @lc code=start
class Solution:
    def countArrangement(self, N: int) -> int:
        
        cache = defaultdict(list)
        for i in range(1, N+1):
            for j in range(1, N+1):
                if i % j == 0 or j % i == 0:
                    cache[i].append(j)
        
        ans = []
        items = []
        nums = list(range(1,N+1))
        visited = set()
        self.dfs(ans, items, N, visited, cache, 1)
        return len(ans)
    
    def dfs(self, ans, items, N, visited, cache, start):
        
        if start > N:
            ans.append(items)
            return
        
        for i in cache[start]:
            if i not in visited:
                visited.add(i)
                self.dfs(ans, items+[i], N, visited, cache, start+1)
                visited.remove(i)
    
    ###########################################################################
    def dfs2(self, ans, items, visited, nums):
        
        if len(items) == len(nums):
            ans.append(items)
        
        for i in range(len(nums)):
            if nums[i] not in visited:
                if (len(items)+1) % nums[i] == 0 or nums[i] % (len(items)+1) == 0:
                    visited.add(nums[i])
                    self.dfs2(ans, items+[nums[i]], visited, nums)
                    visited.remove(nums[i])
    
    def dfs3(self, count, items, visited, nums, start):
        
        if start > len(nums):
            count += 1
        
        for i in range(len(nums)):
            if nums[i] not in visited:
                if start % nums[i] == 0 or nums[i] % start == 0:
                    visited.add(nums[i])
                    self.dfs3(count, items+[nums[i]], visited, nums, start+1)
                    visited.remove(nums[i])
        
# @lc code=end

