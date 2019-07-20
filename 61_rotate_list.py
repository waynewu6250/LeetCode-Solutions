# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head
        
        # Count length
        ptr = head
        length = 0
        while ptr:
            ptr = ptr.next
            length+=1
        if length == 1 or k%length == 0:
            return head
        
        # find split point
        ptr = head
        counter = 1
        while ptr.next != None:
            nxt = ptr.next
            if counter == length - k % length:
                ptr.next = None
                newhead = nxt
            ptr = nxt
            counter+=1
        ptr.next = head
        head = newhead
        
        return head