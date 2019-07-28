#
# @lc app=leetcode id=330 lang=python3
#
# [330] Patching Array
#
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        
        # greedy approach
        # target means we can represent numbers up to target from nums
        
        # Method 1
        target = 1
        res = 0
        i = 0
        while target <= n:
            # we can represent up to target+nums[i]
            if target >= nums[i] and i <= len(nums)-1:
                target += nums[i]
                i += 1
            # we can't use nums[i] which is larger than  target to represent target, we have to add target in nums 
            else:
                target += target
                res += 1
            
        return res


        # Method 2
        target = 1
        i = 0
        original_size = len(nums)
        while target <= n:
            # we can't use nums[i] which is larger than  target to represent target, we have to add target in nums 
            if i >= len(nums) or nums[i] > target:
                nums.insert(i,target)
            # or we can represent up to target+nums[i]
            target += nums[i]
            i+=1
            
        return len(nums)-original_size

