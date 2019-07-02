# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        l = []
        row = [root]
        if root == None:
            return l
        
        while row:
            l.append([node.val for node in row])
            row = [node for root in row for node in (root.left, root.right) if node != None]
            
        
        return l