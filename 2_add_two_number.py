# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Recursive method
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


# Iterative method
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        l1_ptr = l1
        l2_ptr = l2
        dummy = ListNode(-1)
        new_ptr = dummy
        
        carry = 0
        while l1_ptr or l2_ptr:
            
            x = l1_ptr.val if l1_ptr else 0
            y = l2_ptr.val if l2_ptr else 0
            
            s = (x + y + carry) % 10
            
            new_node = ListNode(s)
            new_ptr.next = new_node
            new_ptr = new_node
            
            carry = (x + y + carry) // 10
            
            if l1_ptr:
                l1_ptr = l1_ptr.next
            if l2_ptr:
                l2_ptr = l2_ptr.next
        
        if carry > 0:
            new_ptr.next = ListNode(carry)
        
        
        return dummy.next