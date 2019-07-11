# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 1. Recursive
        def find_path(root, p, q):
            root_val = root.val
            p_val = p.val
            q_val = q.val
            if p_val < root_val and q_val < root_val:
                return find_path(root.left, p, q)
            elif p_val > root_val and q_val > root_val:
                return find_path(root.right, p, q)
            else:
                return root
        return find_path(root, p, q)
    
        # 2. iterative
        def find_path(root, p, q):
            root_val = root.val
            p_val = p.val
            q_val = q.val
            
            while node:
                root_val = node.val
                if p_val < root_val and q_val < root_val:
                    node = node.left
                elif p_val > root_val and q_val > root_val:
                    node = node.right
                else:
                    return node
        return find_path(root, p, q)