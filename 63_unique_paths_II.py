class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # 1. setup dp array: directly use obstacleGrid, check first point
        if obstacleGrid[0][0] == 1:
            return 0
        
        # 2. constraints
        obstacleGrid[0][0] = 1
        
        # first col
        for i in range(1,m):
            # up has one method, and current is not obstacle
            obstacleGrid[i][0] = int(obstacleGrid[i-1][0]==1 and obstacleGrid[i][0]==0)
        # first row
        for j in range(1,n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j-1]==1 and obstacleGrid[0][j]==0)
        
        # 3. for + formula
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0
        
        return obstacleGrid[m-1][n-1]