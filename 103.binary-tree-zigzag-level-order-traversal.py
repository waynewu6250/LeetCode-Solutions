#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return root
        
        def reverse(row):
            a = row.copy()
            for i in range(len(row)//2):
                a[i], a[len(row)-1-i] = a[len(row)-1-i], a[i]
            return a
        
        answer = []
        row = [root]
        counter = 0
        while row:
            if counter % 2 != 0:
                reverse_row = reverse(row)
            else:
                reverse_row = row
            
            answer.append([node.val for node in reverse_row])
            row = [node for root in row for node in (root.left,root.right) if node != None]
            
            counter += 1
            
        
        return answer


        ################################################################r
        # queue method
        if not root:
            return []
        
        from collections import deque
        queue = deque([root])
        answer = []
        items = []
        rounds = 0
        
        while queue:
            
            items = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                items.append(node.val)
            
            answer.append(items if rounds % 2 ==0 else items[::-1])
            rounds+=1
        
        return answer
        

