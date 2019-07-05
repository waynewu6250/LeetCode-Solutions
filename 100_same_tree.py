# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def find(rootA, rootB):
            if rootA == None and rootB == None: return True
            if rootA == None or rootB == None: return False
            else: return (rootA.val == rootB.val) and \
                find(rootA.left, rootB.left) and \
                find(rootA.right, rootB.right)
        return find(p,q)