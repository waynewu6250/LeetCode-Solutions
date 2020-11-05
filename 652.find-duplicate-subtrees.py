#
# @lc app=leetcode id=652 lang=python3
#
# [652] Find Duplicate Subtrees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        cache = {}
        ans = []
        self.dfs(root, ans, cache)
        return ans
        
    def dfs(self, root, ans, cache):
        
        if not root:
            return None
        
        left = self.dfs(root.left, ans, cache)
        right = self.dfs(root.right, ans, cache)
        serial = '{},{},{}'.format(root.val, left, right)
        
        cache[serial] = cache.get(serial,0) + 1
        if cache[serial] == 2:
            ans.append(root)
        
        return serial
        
# @lc code=end

