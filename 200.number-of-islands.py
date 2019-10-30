#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
class Solution:
    # dfs method
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        
        ans = 0
        for y in range(m):
            for x in range(n):
                if grid[y][x] == '1':
                    ans += 1
                    self.__dfs(grid, x, y, n, m)
        return ans
    
    def __dfs(self, grid, x, y, n, m):
        if x < 0 or y < 0 or x >=n or y >= m or grid[y][x] == '0':
            return
        grid[y][x] = '0'
        self.__dfs(grid, x + 1, y, n, m)
        self.__dfs(grid, x - 1, y, n, m)
        self.__dfs(grid, x, y + 1, n, m)
        self.__dfs(grid, x, y - 1, n, m)
    

    #################################################
    # bfs method (recommended)
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        if not grid or not grid[0]:
            return 0
        
        islands = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    self.bfs(grid, x, y)
                    islands += 1
        return islands
    
    
    def bfs(self, grid, x, y):
        
        queue = collections.deque([(x,y)])
        grid[x][y] = '0'
        
        while queue:
            x, y = queue.popleft()
            for x_inc, y_inc in [(1,0), (0,1), (-1,0), (0,-1)]:
                x_new = x + x_inc
                y_new = y + y_inc
                if not (0 <= x_new < len(grid) and 0 <= y_new < len(grid[0]) and grid[x_new][y_new] == '1'):
                    continue
                queue.append((x_new, y_new))
                grid[x_new][y_new] = '0'

        

