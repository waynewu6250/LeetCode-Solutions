#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        left_last = self.flatten(root.left)
        right_last = self.flatten(root.right)
        
        if left_last is not None:
            left_last.right = root.right
            root.right = root.left
            root.left = None
        
        if right_last is not None:
            return right_last
        if left_last is not None:
            return left_last
        return root
        
# @lc code=end

