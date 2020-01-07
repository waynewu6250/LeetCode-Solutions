class Solution:

    def two_difference(self, nums : List[int], target: int) -> List[int]:

        nums.sort()

        j = 1
        for i in range(len(nums)):
            while j < len(nums) and nums[j]-nums[i] < target:
                j += 1
            if nums[j]-nums[i] == target:
                return [i, j]