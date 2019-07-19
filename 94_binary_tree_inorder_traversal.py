# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 1. recursive
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        l = []
        def inorder(root):
            if root != None:
                inorder(root.left)
                l.append(root.val)
                inorder(root.right)
        inorder(root)
        return l

    # 2. iterative
    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        
        answer = []
        stack = []
        if root == None:
            return answer
        
        while root != None or stack:
            
            #1. Push all left node to stack
            while root:
                stack.append(root)
                root = root.left
            
            #2. get root from stack
            root = stack.pop(-1)
            answer.append(root.val)
            
            #3. move to right node
            root = root.right
        
        return answer