#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        def recur(root, ind):
            if not root:
                return 0
            if not root.left and not root.right and ind:
                return root.val
            return recur(root.left, 1) + recur(root.right, 0)
        
        return recur(root, 0)
        

