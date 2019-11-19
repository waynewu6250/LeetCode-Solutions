#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answer = []
        rows = []
        self.dfs(answer, rows, n)
        return answer
    
    def dfs(self, answer, rows, n):
        # current row
        row = len(rows)
        
        if row == n:
            answer.append(self.draw_board(rows))
            return
        
        for col in range(n):
            if not self.is_valid(rows, row, col):
                continue
            self.dfs(answer, rows + [col], n)
    
    def is_valid(self, rows, row, col):
        for r, c in enumerate(rows):
            # verify columns
            if c == col:
                return False
            # verify diagonal
            if r - c == row - col or r + c == row + col:
                return False
        return True
    
    def draw_board(self, rows):
        n = len(rows)
        board = []
        for i in range(n):
            row = ['Q' if j == rows[i] else '.' for j in range(n)]
            board.append(''.join(row))
        return board
        
# @lc code=end

