#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # 1. '1'
        # 2. visited = (grid[x][y] == 0)
        
        if not grid or not grid[0]:
            return 0
        
        ans = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    ans += 1
                    #self.bfs(grid, i, j)
                    self.dfs(grid, i, j)
        return ans
    
    # dfs approach
    def dfs(self, grid, i, j):
        
        if not (0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1'):
            return
        
        grid[i][j] = '0'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)

    
    # bfs approach
    def bfs(self, grid, i, j):
        
        queue = collections.deque([(i,j)])
        grid[i][j] = '0'
        
        while queue:
            (x, y) = queue.popleft()
            
            for x_inc, y_inc in [(0,1), (0,-1), (1,0), (-1,0)]:
                x_new = x + x_inc
                y_new = y + y_inc
                
                if 0 <= x_new < len(grid) and 0 <= y_new < len(grid[0]) and grid[x_new][y_new] == '1':
                    queue.append((x_new, y_new))
                    grid[x_new][y_new] = '0'

        

