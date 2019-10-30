#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if not prerequisites:
            return range(numCourses)
        
        # 1. get nodes' indegree
        node_to_indegree = {i:0 for i in range(numCourses)}
        for course, _ in prerequisites:
            node_to_indegree[course] = node_to_indegree[course]+1
        
        # 2. find start nodes with 0 indegree and put it into queue
        order = []
        startpoints = [k for k,v in node_to_indegree.items() if v == 0]
        
        queue = collections.deque(startpoints)
        
        # 3. bfs
        while queue:
            node = queue.popleft()
            order.append(node)
            
            for course, prereq in prerequisites:
                if prereq == node:
                    node_to_indegree[course] -= 1
                    if node_to_indegree[course] == 0:
                        queue.append(course)
        
        return order if len(order) == numCourses else []
        
# @lc code=end

