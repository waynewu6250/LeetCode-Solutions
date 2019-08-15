#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:

        row = [root]
        answer = []
        while row:
            nums = [node.val for node in row]
            answer.append(sum(nums)/len(nums))
            row = [node for root in row for node in (root.left, root.right) if node != None]
        
        return answer
        

