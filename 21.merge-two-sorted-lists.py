#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if not l1:
            return l2
        if not l2:
            return l1
        
        ptr1 = l1
        ptr2 = l2
        dummy = ListNode(-1)
        ptr = dummy
        
        while ptr1 != None and ptr2 != None:
            if ptr1.val < ptr2.val:
                ptr.next = ptr1
                ptr1 = ptr1.next
            else:
                ptr.next = ptr2
                ptr2 = ptr2.next
            
            ptr = ptr.next
        
        if ptr1 == None:
            ptr.next = ptr2
        else:
            ptr.next = ptr1
            
        return dummy.next
        
# @lc code=end

