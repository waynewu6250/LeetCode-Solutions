#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # # 1. solution 1: sort
        # nums.sort()
        # return nums[-k]

        # # 2. solution 2: maxheap
        # nums = [-num for num in nums]
        # import heapq
        # heapq.heapify(nums)
        # for _ in range(k):
        #     res = heapq.heapify(nums)
        # return -res
        
        # 3. solution 3: minheap: maintain k largest elements
        import heapq
        array = nums[:k]
        heapq.heapify(array)
        
        for i in range(k, len(nums)):
            if nums[i] > array[0]:
                heapq.heappop(array)
                heapq.heappush(array, nums[i])
        
        return array[0]

        # 4. quick select
        n = len(nums)
        k = n-k
        
        return self.partition(nums, 0, n-1, k)
    
    def partition(self, nums, start, end, k):
        
        left = start
        right = end
        pivot = nums[left]
        
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        if k <= right:
            return self.partition(nums, start, right, k)
        if k >= left:
            return self.partition(nums, left, end, k)
        
        return nums[k]
       




        

