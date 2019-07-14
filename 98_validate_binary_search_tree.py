# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 1. recursive
class Solution1:
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

# 2. iterative
class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        answer = []
        stack = []
        prev = None
        if root == None:
	        return answer
	        
        while root != None or stack:
	            
            #1. Push all left node to stack
            while root:
                stack.append(root)
                root = root.left
            
            #2. get root from stack
            root = stack.pop(-1)
            
            #3. check prev and root
            if prev != None and prev.val >= root.val: return False
            prev = root
            #3. move to right node
            root = root.right
	    
        return answer

        