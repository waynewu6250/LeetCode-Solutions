def quicksort(self, nums: List[int]) -> List[int]:
    
		self.partition(nums, 0, n-1)
    return nums

def partition(self, nums, start, end):
    
    left = start
    right = end
    pivot = nums[left]
    
		# 將當前小於left和大於right的排好序
    while left <= right:
        while left <= right and nums[left] < pivot:
            left += 1
        while left <= right and nums[right] > pivot:
            right -= 1
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    
		# 分治法
    self.partition(nums, start, right)
    self.partition(nums, left, end)