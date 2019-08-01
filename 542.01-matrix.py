#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

        if len(matrix) == 0:
            return matrix
       
        m = len(matrix)
        n = len(matrix[0])
        
        
        # method 1: bfs
        q = collections.deque()
        
        # 1. Put 0 in queue
        dist = [[float('inf')]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                    q.append((i,j))
        
        # 2. search nodes
        iterators = [(0,1), (0,-1), (1,0), (-1,0)]
        while q:
            row, col = q.popleft()
            for i in range(len(iterators)):
                new_r = row + iterators[i][0]
                new_c = col + iterators[i][1]
                
                if new_r >= 0 and new_r < m and new_c >= 0 and new_c < n:
                    if dist[new_r][new_c] > dist[row][col]+1:
                        dist[new_r][new_c] = dist[row][col]+1
                        q.append((new_r,new_c))
        
        return dist
    
        # method 2: dp method: the shortest distance from 0 to current position
        dp = [[float('inf')]*n for _ in range(m)]
        # from top and left
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] = min(dp[i][j], dp[i-1][j]+1)
                    if j > 0:
                        dp[i][j] = min(dp[i][j], dp[i][j-1]+1)
        
        # from bottom and right
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i < m-1:
                    dp[i][j] = min(dp[i][j], dp[i+1][j]+1)
                if j < n-1:
                    dp[i][j] = min(dp[i][j], dp[i][j+1]+1)
        
        return dp
        

