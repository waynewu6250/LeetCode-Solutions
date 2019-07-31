#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        if not nums:
            return False
        
        cache = {}
        for i, num in enumerate(nums):
            if num not in cache:
                cache[num] = [i]
            else:
                for index in cache[num]:
                    if i - index <= k:
                        return True
                cache[num] = cache[num] + [i]
        return False
        

