#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return
        
        first = None
        last = None
        head = root
        while head:
            
            # 1. Set first node
            if not first:
                if head.left:
                    first = head.left
                elif head.right:
                    first = head.right
            
            # 2. Set left and right node
            if head.left:
                if last:
                    last.next = head.left
                last = head.left
            if head.right:
                if last:
                    last.next = head.right
                last = head.right
            
            # 3. Set root
            if head.next:
                # We have done this tree
                head = head.next
            else:
                # We haven't done this tree
                head = first
                first = None
                last = None
            
        
        return root
        

