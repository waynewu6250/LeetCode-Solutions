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
        if not root:
            return 0
        
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)    
        if l == 0:
            return r + 1
        if r == 0:
            return l + 1

        return min(l, r) + 1