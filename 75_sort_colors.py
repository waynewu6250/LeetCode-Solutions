class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # O(N) space
        counts = {}
        for i in nums:
            counts[i] = counts.get(i,0) + 1
        index = 0
        for k,v in counts.items():
            for _ in range(v):
                nums[index] = k
                index += 1
        
        # O(1) space
        for i in range(len(nums)):
            k = 0
            while k < i:
                if nums[i] < nums[k]:
                    tmp = nums[i]
                    nums[i] = nums[k]
                    nums[k] = tmp
                k += 1