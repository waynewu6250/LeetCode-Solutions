#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        if not board or not board[0]:
            return []
        
        prefix_set = set()
        for i in range(len(word)):
            prefix_set.add(word[:i + 1])
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if self.search( board, x, y, board[x][y], word, prefix_set, set([(x, y)]) ):
                    return True
        return False
        
        
    def search(self, board, x, y, cur_word, word, prefix_set, visited ):
        
        if cur_word not in prefix_set:
            return
        if cur_word == word:
            return True
        
        for (x_inc, y_inc) in [(0,1), (0,-1), (1,0), (-1,0)]:
            x_new = x + x_inc
            y_new = y + y_inc
            
            if not self.inside(board, x_new, y_new):
                continue
            if (x_new, y_new) in visited:
                continue
            visited.add((x_new, y_new))
            if self.search( board, x_new, y_new, cur_word+board[x_new][y_new], word, prefix_set, visited ):
                return True
            visited.remove((x_new, y_new))
        return False
    
    def inside(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])
# @lc code=end

