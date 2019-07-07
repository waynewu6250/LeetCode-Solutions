# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        row = [root]
        while row:
            ans.append([node.val for node in row])
            row = [node for root in row for node in (root.left, root.right) if node != None]
        return ans[::-1]