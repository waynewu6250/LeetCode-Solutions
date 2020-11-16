#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

        if not root:
            return []
        
        queue = deque([root])
        
        ans = []
        while queue:
            items = []
            for i in range(len(queue)):
                root = queue.popleft()
                items.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            ans.append(items[-1])
                
        return ans
        
# @lc code=end
