# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 1. recursive
class Solution1:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        l = []
        def preorder(root):
            if root != None:
                l.append(root.val)
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return l

# 2. iterative + stack
class Solution2:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        answer = []
        stack = []
        if root == None:
            return answer
        
        stack.append(root)

        while stack:
            root = stack.pop(-1)
            if root:
                stack.append(root.right)
                stack.append(root.left)
                answer.append(root.val)
        
        return answer
