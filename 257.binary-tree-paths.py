#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        answer = []
        items = ""
        
        def recur(items, root):
            if not root:
                return
            if not root.left and not root.right:
                answer.append(items + str(root.val))
            
            recur(items + str(root.val) + "->", root.left)
            recur(items + str(root.val) + "->", root.right)
            
        
        recur(items, root)
        return answer
        
# @lc code=end

