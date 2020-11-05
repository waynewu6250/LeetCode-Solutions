#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:

        # dfs
        cache = defaultdict(list)
        def dfs(root, level):
            if root:
                dfs(root.left, level+1)
                cache[level].append(root.val)
                dfs(root.right, level+1)
        dfs(root, 1)
        
        cache = sorted(cache.items(), key = lambda x: x[0])
        return [max(v) for k, v in cache]
            
        # bfs
        if not root:
            return []
        
        queue = deque([root])
        answer = [root.val]
        
        while queue:
            items = []
            for i in range(len(queue)):
                root = queue.popleft()
                if root.left:
                    items.append(root.left.val)
                    queue.append(root.left)
                if root.right:
                    items.append(root.right.val)
                    queue.append(root.right)
            if items:
                answer.append(max(items))
        
        return answer
        
# @lc code=end

