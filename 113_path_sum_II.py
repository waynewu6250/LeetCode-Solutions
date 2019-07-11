# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        items = []
        results = []
        
        def dfs(root, s):
            if root:
                items.append(root.val)
                dfs(root.left, s)
                dfs(root.right, s)
                if not root.left and not root.right and sum(items) == s:
                    results.append(items[:])
                items.pop()
        
        dfs(root, s)
        return results