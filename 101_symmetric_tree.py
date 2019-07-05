# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        # 1. Recursive
        def recursive(rootA, rootB):
            if rootA == None and rootB == None:
                return True
            if rootA == None or rootB == None:
                return False
            else: return (rootA.val == rootB.val) and \
                recursive(rootA.left, rootB.right) and \
                recursive(rootA.right, rootB.left)
            return recursive(root,root)
    
        # 2. Iterative
        row = [root, root]
        while row:
            rootA = row.pop(0)
            rootB = row.pop(0)
            if rootA == None and rootB == None:
                continue
            if rootA == None or rootB == None:
                return False
            if rootA.val != rootB.val:
                return False
            row += [rootA.left, rootB.right, rootA.right, rootB.left]
        return True
                