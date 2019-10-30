#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        node_to_indegree = {i:0 for i in range(numCourses)}
        for course, _ in prerequisites:
            node_to_indegree[course] = node_to_indegree[course]+1
        
        order = []
        startpoints = [k for k,v in node_to_indegree.items() if v == 0]
        
        queue = collections.deque(startpoints)
        
        while queue:
            node = queue.popleft()
            order.append(node)
            
            for course, prereq in prerequisites:
                if prereq == node:
                    node_to_indegree[course] -= 1
                    if node_to_indegree[course] == 0:
                        queue.append(course)
        
        return len(order) == numCourses
        
# @lc code=end

