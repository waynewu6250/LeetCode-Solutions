#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        def recur(root, target):
            
            if not root:
                return False
            
            if not root.left and not root.right and target == root.val:
                return True
            
            return recur(root.left, target-root.val) or recur(root.right, target-root.val)
        
        return recur(root, sum)


        
# @lc code=end

