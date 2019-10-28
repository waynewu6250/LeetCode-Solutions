# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        # Use list comprehension
        l = []
        row = [root]
        if root == None:
            return l
        
        while row:
            l.append([node.val for node in row])
            row = [node for root in row for node in (root.left, root.right) if node != None]
        return l

        # Use queue
        from collections import deque
        
        if not root:
            return []
        
        queue = deque([root])
        answer = []
        level = []
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                level.append(node.val)
            answer.append(level)
        
        return answer

            
        
        