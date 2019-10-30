#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        prev = dummy
        ptr = head
        
        while ptr and ptr.next:
            # save head.next
            nxt = ptr.next
            
            # swap
            ptr.next = nxt.next
            nxt.next = ptr
            prev.next = nxt
            
            # proceed
            prev = ptr
            ptr = ptr.next
        
        return dummy.next
        
        
#         def recur(head):
#             if head == None or head.next == None:
#                 return head
            
#             nxt = head.next
#             head.next = recur(nxt.next)
#             nxt.next = head
            
#             return nxt
#         return recur(head)
        
# @lc code=end

