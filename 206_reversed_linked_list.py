# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Iteratively
        prev = None
        ptr = head
        
        while ptr != None:
            next = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = next
            
        return prev

        # Recursively
        if head == None or head.next == None:
            return head
        ptr = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return ptr