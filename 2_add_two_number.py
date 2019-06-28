# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode: 
        
        def add(l1, l2, carry):
            
            if l1 == None and l2 == None and carry == 0:
                return None
            
            value = carry
            if l1 != None:
                value += l1.val
            if l2 != None:
                value += l2.val
            
            result = ListNode(value%10)
            
            if l1 != None or l2 != None:
                
                result.next = add(l1.next if l1 != None else None,l2.next if l2 != None else None,int(value/10))
            
            return result
        
        return add(l1,l2,0)