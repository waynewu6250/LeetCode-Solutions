#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        root = node
        if not node:
            return node
        
        # 1. Use bfs to get all the nodes
        nodes = self.get_nodes(node)
        
        # 2. Copy nodes
        mapping = {node: Node(node.val, []) for node in nodes}
        
        # 3. Copy neighbors
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)
        
        return mapping[root]
        
    
    def get_nodes(self, node):
        
        queue = deque([node])
        revisited = set([node])
       
        while queue:
            head = queue.popleft()
            for neighbor in head.neighbors:
                if neighbor not in revisited:
                    revisited.add(neighbor)
                    queue.append(neighbor)
        return revisited
        
# @lc code=end

