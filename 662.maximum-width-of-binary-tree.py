#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:

        queue = collections.deque([(root, 1)])
        answer = 1
        
        while queue:
            answer = max(answer, queue[-1][1] - queue[0][1] + 1)
            for i in range(len(queue)):
                node, pos = queue.popleft()
                if node.left:
                    queue.append((node.left, 2*pos))
                if node.right:
                    queue.append((node.right, 2*pos+1))
        
        return answer
        
# @lc code=end

