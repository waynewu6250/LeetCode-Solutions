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
        self.dfs(root, answer, items, sum)
        return answer
    
    def dfs(self, root, answer, items, sum):
        
        if not root:
            return
        
        if not root.left and not root.right and sum == root.val:
            answer.append(items+[root.val])
            return
        
        self.dfs(root.left, answer, items+[root.val], sum-root.val)
        self.dfs(root.right, answer, items+[root.val], sum-root.val)
        
# @lc code=end

