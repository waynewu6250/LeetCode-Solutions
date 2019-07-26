# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 1.root condition
        if not root:
            return 0
        # 2.root.left, right condition
        if not root.left and not root.right:
            return 1
        
        # 3.recursive
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)    
        
        # 2.root.left, right condition
        if not root.left:
            return r + 1
        if not root.right:
            return l + 1
        
        # 4.root,left,right comparison
        return min(l, r) + 1