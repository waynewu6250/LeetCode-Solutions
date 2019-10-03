#
# @lc app=leetcode id=606 lang=python3
#
# [606] Construct String from Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        
        def recur(root):
            if not root:
                return ""
            if not root.left and not root.right:
                return str(root.val)
            if not root.right:
                return str(root.val)+"("+recur(root.left)+")";
            else:
                return str(root.val)+"("+recur(root.left)+")("+recur(root.right)+")"
        
        return recur(t)
        

