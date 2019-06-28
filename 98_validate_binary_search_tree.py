# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.checkBST(root, None, None)
    
    def checkBST(self, root, min_, max_):
        if root == None:
            return True
        
        if (min_ != None and root.val <= min_) or (max_ != None and root.val >= max_):
            return False
        
        if (self.checkBST(root.left, min_, root.val) == False) or (self.checkBST(root.right, root.val, max_) == False):
            return False
        
        return True