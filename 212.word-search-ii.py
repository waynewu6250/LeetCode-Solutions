#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        if not board or not board[0]:
            return []
        if not words:
            return []
        
        word_set = set(words)
        prefix_set = set()
        for word in words:
            for i in range(len(word)):
                prefix_set.add(word[:i + 1])
        
        results = []
        for x in range(len(board)):
            for y in range(len(board[0])):
                self.search( board, x, y, board[x][y], word_set, prefix_set, results, set([(x, y)]) )
        return list(set(results))
        
    def search(self, board, x, y, cur_word, word_set, prefix_set, results, visited ):
        
        if cur_word not in prefix_set:
            return
        if cur_word in word_set:
            results.append(cur_word)
        
        for (x_inc, y_inc) in [(0,1), (0,-1), (1,0), (-1,0)]:
            x_new = x + x_inc
            y_new = y + y_inc
            
            if not self.inside(board, x_new, y_new):
                continue
            if (x_new, y_new) in visited:
                continue
            visited.add((x_new, y_new))
            self.search( board, x_new, y_new, cur_word+board[x_new][y_new], word_set, prefix_set, results, visited )
            visited.remove((x_new, y_new))
    
    def inside(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])
        
# @lc code=end

