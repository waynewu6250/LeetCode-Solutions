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
        min_heap = [-float('inf')]*k
        heapq.heapify(min_heap)
        for num in nums:
            if num > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)
        return min_heap[0]

       




        

