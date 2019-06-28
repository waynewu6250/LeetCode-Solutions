# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def get_length(head):
            length = 0
            end = None
            ptr = head
            while ptr != None:
                end = ptr
                ptr = ptr.next
                length += 1
            return length, end
        
        lengthA, endA = get_length(headA)
        lengthB, endB = get_length(headB)
        
        if endA != endB:
            return None
        
        diff = lengthA - lengthB
        cut = abs(diff)
        if diff < 0:
            while cut != 0:
                headB = headB.next
                cut -= 1
        else:
            while cut != 0:
                headA = headA.next
                cut -= 1
        
        while headA != None and headB != None:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next