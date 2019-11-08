#
# @lc app=leetcode id=653 lang=python3
#
# [653] Two Sum IV - Input is a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:

        if not root:
            return False
        
        items = []
        def inorder(root):
            if root:
                inorder(root.left)
                items.append(root.val)
                inorder(root.right)
        inorder(root)
        
        left = 0
        right = len(items)-1
        
        while left < right:
            sum = items[left] + items[right]
            if sum == k:
                return True
            elif sum < k:
                left+=1
            else:
                right-=1
        return False
        
# @lc code=end

