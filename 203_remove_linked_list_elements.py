# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # Use dummy node
        if head == None:
            return None
        
        dummy = ListNode(float('inf'))
        dummy.next = head
        
        cur = head
        prev = dummy
        
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        
        return dummy.next

        # Not using dummy node
        if not head:
            return head
        
        ptr = head
        while ptr.next:
            if ptr.next.val == val:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        return head.next if head.val == val else head
