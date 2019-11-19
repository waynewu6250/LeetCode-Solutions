class Solution(object):
    # Method 1
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
    
    # Method 2
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index = self.sort(nums, 0, 0)
        self.sort(nums, 1, index)
        
    def sort(self, nums, flag, index):
        start, end = index, len(nums) - 1
        while start <= end:
            while start <= end and nums[start] == flag:
                start += 1
            while start <= end and nums[end] != flag:
                end -= 1
            if start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        return start