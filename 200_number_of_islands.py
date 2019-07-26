class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        
        ans = 0
        for y in xrange(m):
            for x in xrange(n):
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