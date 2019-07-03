# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        
        odd_ptr = head
        even_ptr = head.next
        even_head = head.next
        
        while even_ptr != None and even_ptr.next != None:
            
            odd_ptr.next = even_ptr.next
            odd_ptr = odd_ptr.next
            even_ptr.next = odd_ptr.next
            even_ptr = even_ptr.next
        
        odd_ptr.next = even_head
        
        return head
            