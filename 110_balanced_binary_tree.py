# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def get_height(self,root):
        if root == None:
            return -1
        else: return max(self.get_height(root.left), self.get_height(root.right))+1
		
    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        
        diff = abs(self.get_height(root.right)-self.get_height(root.left))
        if diff > 1:
            return False
        else: return self.isBalanced(root.left) and self.isBalanced(root.right)

##################################################################################

class Solution2:
    def isBalanced(self, root: TreeNode) -> bool:

        return self.check_height(root) != -1
    
    def check_height(self, root):
        
        if not root:
            return 0
        
        # if false return directly, no need to compare
        left_height = self.check_height(root.left)
        right_height = self.check_height(root.right)
        
        if left_height == -1 or right_height == -1:
            return -1
        
        # if not, compare
        diff = abs(left_height-right_height)
        if diff > 1:
            return -1
        else:
            return max(left_height, right_height)+1