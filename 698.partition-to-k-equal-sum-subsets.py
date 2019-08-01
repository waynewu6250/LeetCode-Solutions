#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        nums = sorted(nums)
        target = sum(nums) / k
        
        # 1. precheck
        while nums[-1] >= target:
            if nums[-1] > target:
                return False
            else:
                nums.pop()
                k -= 1
        
        # 2. set up k groups, for each group has sum target
        def search(groups):
            
            if not nums: 
                return True
            
            v = nums.pop()
            for i, group in enumerate(groups):
                if group + v <= target:
                    groups[i] += v
                    if search(groups): return True
                    groups[i] -= v
                if not group:
                    break
            nums.append(v)
            return False
            
        return search([0]*k)
        

