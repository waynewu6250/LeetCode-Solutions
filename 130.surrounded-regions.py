#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
    
        if not board:
            return None
        
        m = len(board)
        n = len(board[0])
        
        def dfs(i,j):
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = '*'
                list(map(dfs, (i,i,i+1,i-1), (j+1,j-1,j,j)))
        
        for i in range(m):
            list(map(dfs, (i, i), (0, n - 1)))

        for i in range(n):
            list(map(dfs, (0, m - 1), (i, i)))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '*':
                    board[i][j] = 'O'
        
        return board
        

