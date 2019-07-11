# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        items = []
        results = []
        def dfs(root):
            if root:
                items.append(root.val)
                dfs(root.left)
                dfs(root.right)
                if not root.left and not root.right:
                    results.append(sum([num*(10**i) for i, num in enumerate(items[::-1])]))
                items.pop()
        dfs(root)
        return sum(results)