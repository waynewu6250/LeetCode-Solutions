# Method 1
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
            
            if self.inside(board, x_new, y_new) and (x_new, y_new) not in visited:
                visited.add((x_new, y_new))
                if self.search( board, x_new, y_new, cur_word+board[x_new][y_new], word, prefix_set, visited ):
                    return True
                visited.remove((x_new, y_new))
            
        return False
    
    def inside(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])

# Method 2
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        k = len(word)
        
        # Precheck
        cache = {}
        for i in range(m):
            for j in range(n):
                cache[board[i][j]] = cache.get(board[i][j],0)+1
        
        for char in word:
            if char in cache:
                if cache[char] < 0:
                    return False
                cache[char] = cache[char] - 1
            else:
                return False
        
        # DFS
        def dfs(x, y, length):
            if length == k:
                return True
            if 0 <= x < m and 0 <= y < n and board[x][y] == word[length]:
                board[x][y] = None
                match = dfs(x,y+1,length+1) or dfs(x+1,y,length+1) or dfs(x,y-1,length+1) or dfs(x-1,y,length+1)
                board[x][y] = word[length]
                return match
        
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0): return True
        return False