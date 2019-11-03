#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        answer = []
        items = []
        
        def recur(root, target, items):
            
            if not root:
                return False
            
            if not root.left and not root.right and target == root.val:
                answer.append(items + [root.val])
            
            recur(root.left, target-root.val, items+[root.val])
            recur(root.right, target-root.val, items+[root.val])
        
        recur(root, sum, items)
        return answer
        
# @lc code=end

