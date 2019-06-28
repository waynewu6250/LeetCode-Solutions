class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            nums = nums
        else:
            count = 0
            prev = nums[len(nums)-1]
            for i in range(len(nums)-2,-1,-1):
                if nums[i] == prev:
                    count += 1
                    if count > 1:
                        nums.pop(i)
                else:
                    prev = nums[i]
                    count = 0