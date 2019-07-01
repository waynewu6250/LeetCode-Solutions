# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        l = []
        def preorder(root):
            if root != None:
                l.append(root.val)
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return l