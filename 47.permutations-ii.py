#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        
        answer = []
        items = []
        
        def recur(items, numbers):
            if len(items) == len(nums):
                answer.append(items)
                
            for i in range(len(numbers)):
                if i > 0 and numbers[i] == numbers[i-1]:
                    continue
                recur(items + [numbers[i]], numbers[:i]+numbers[i+1:])
        
        recur(items, nums)
        return answer


        
# @lc code=end

