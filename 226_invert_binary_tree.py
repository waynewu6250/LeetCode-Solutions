# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #1. recursive
        def invert(root):
            if root == None:
                return None
            left = invert(root.left)
            right = invert(root.right)
            root.left = right
            root.right = left
            return root
        return invert(root)
    
        #2. iterative
        def iterative(root):
            if root == None:
                return None
            row = [root]
            while row:
                cur = row.pop(0)
                tmp = cur.left
                cur.left = cur.right
                cur.right = tmp
                
                if cur.left != None: row.append(cur.left)
                if cur.right != None: row.append(cur.right)
            return root
        return iterative(root)