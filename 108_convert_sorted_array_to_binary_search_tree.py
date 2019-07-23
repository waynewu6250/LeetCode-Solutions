# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def recur(nums, start, end):
            if start > end:
                return None
            mid = (start+end+1) / 2 
            newnode = TreeNode(nums[mid])
            newnode.left = recur(nums, start, mid-1)
            newnode.right = recur(nums, mid+1, end)
            return newnode
        return recur(nums, 0, len(nums)-1)