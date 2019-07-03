# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        
        ptr = head
        
        while ptr != None and ptr.next != None:
            if ptr.next.val == ptr.val:
                next = ptr.next
                ptr.val = next.val
                ptr.next = next.next
            else:
                ptr = ptr.next
        
        return head