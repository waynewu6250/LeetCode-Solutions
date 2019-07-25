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