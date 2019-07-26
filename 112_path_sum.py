# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # 1. traversal
        items = []
        results = []
        
        def dfs(root):
            if root:
                items.append(root.val)
                dfs(root.left)
                dfs(root.right)
                if not root.left and not root.right:
                    results.append(sum(items))
                items.pop()
        
        dfs(root)
        return (s in results)
        
        # 2. left and right tree
        def recur(root, s):
            if not root:
                return False
            if not root.left and not root.right:
                return root.val == s
            l = recur(root.left,s-root.val)
            r = recur(root.right,s-root.val)
            return l or r
        return recur(root,s)