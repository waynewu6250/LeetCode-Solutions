#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
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

        def recur(root):
            if not root:
                return
            if not root.left and not root.right:
                return
            
            if root.left:
                root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            
            recur(root.left)
            recur(root.right)

        
        recur(root)
        return root

        

