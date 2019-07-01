# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        l = []
        def postorder(root):
            if root != None:
                postorder(root.left)
                postorder(root.right)
                l.append(root.val)
        postorder(root)
        return l