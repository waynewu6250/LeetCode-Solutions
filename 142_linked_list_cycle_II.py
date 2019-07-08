# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
                
        if fast == None or fast.next == None:
            return None
        
        # Put slow back to head
        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast