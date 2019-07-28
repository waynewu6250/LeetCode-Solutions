#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return board
        
        m = len(board)
        n = len(board[0])
        
        oldboard = [[0]*(n+2) for _ in range(m+2)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                oldboard[i][j] = board[i-1][j-1]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                  
                counts = oldboard[i-1][j-1] + oldboard[i][j-1] + oldboard[i+1][j-1] + \
                         oldboard[i-1][j] + oldboard[i+1][j] + \
                         oldboard[i-1][j+1] + oldboard[i][j+1] + oldboard[i+1][j+1]
                if oldboard[i][j] == 0 and counts == 3:
                    board[i-1][j-1] = 1
                if oldboard[i][j] == 1:
                    if counts < 2 or counts > 3:
                        board[i-1][j-1] = 0

        

