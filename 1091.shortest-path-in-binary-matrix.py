#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#

# @lc code=start
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if not grid or not grid[0] or grid[0][0] == 1:
            return -1
        
        
        queue = deque([(0,0,1)])
        grid[0][0] = 1
        
        while queue:
            x, y, level = queue.popleft()
            
            if x == len(grid)-1 and y == len(grid[0])-1:
                return level
            
            for x_inc, y_inc in [(0,1), (1,0), (0,-1), (-1,0), (-1,-1), (1,1), (-1,1), (1,-1)]:
                x_new = x + x_inc
                y_new = y + y_inc
                if 0 <= x_new < len(grid) and 0 <= y_new < len(grid[0]) and grid[x_new][y_new] == 0:
                    queue.append((x_new, y_new, level+1))
                    grid[x_new][y_new] = '1'
                    
        return -1
        
# @lc code=end

