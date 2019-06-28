class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            nums = nums
        else:
            prev = nums[len(nums)-1]
            for i in range(len(nums)-2,-1,-1):
                if nums[i] == prev:
                    nums.pop(i)
                else:
                    prev = nums[i]
