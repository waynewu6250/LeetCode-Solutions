#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        if not head:
            return head
        
        ptr = head
        dummyA = ListNode(0)
        dummyB = ListNode(0)
        ptrA = dummyA
        ptrB = dummyB
        
        while ptr:
            if ptr.val < x:
                ptrA.next = ptr
                ptrA = ptrA.next
            else:
                ptrB.next = ptr
                ptrB = ptrB.next
            ptr = ptr.next
        
        ptrB.next = None
        ptrA.next = dummyB.next
        
        return dummyA.next
        

