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
        
        # 3. solution 3: minheap-maintain k largest elements
        import heapq
        array = nums[:k]
        heapq.heapify(array)
        
        for i in range(k, len(nums)):
            if nums[i] > array[0]:
                heapq.heappop(array)
                heapq.heappush(array, nums[i])
        
        return array[0]

       




        

