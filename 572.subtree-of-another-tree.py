#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        if self.isSametree(s, t):
            return True
        if not s:
            return False
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def isSametree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return self.isSametree(s.left,t.left) and self.isSametree(s.right,t.right) and s.val == t.val
        
# @lc code=end

