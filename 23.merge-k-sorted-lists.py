#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        if not lists:
            return None
        count = 0
        
        heap = []
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, count, l))
                count += 1
        
        dummy = ListNode(-1)
        tail = dummy
        
        while heap:
            _, _, tail.next = heapq.heappop(heap)
            tail = tail.next
            if tail.next:
                heapq.heappush(heap, (tail.next.val, count+1, tail.next))
                count += 1
        return dummy.next
        
# @lc code=end

