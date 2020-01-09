#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        
        answer = []
        rows = []
        self.dfs(answer, rows, n)
        return len(answer)
    
    def dfs(self, answer, rows, n):
        
        row = len(rows)
        
        if row == n:
            answer.append(rows)
        
        for col in range(n):
            if self.check_board(rows, row, col):
                self.dfs(answer, rows + [col], n)
    
    def check_board(self, rows, row, col):
        
        for r,c in enumerate(rows):
            if c == col:
                return False
            if r-c == row-col or r+c == row+col:
                return False
        
        return True
        
# @lc code=end

