# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        l = []
        def inorder(root):
            if root != None:
                inorder(root.left)
                l.append(root.val)
                inorder(root.right)
        inorder(root)
        return l