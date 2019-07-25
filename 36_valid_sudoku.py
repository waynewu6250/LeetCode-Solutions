class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        table = {"rows": [set() for _ in range(9)], "columns": [set() for _ in range(9)], "squares": [set() for _ in range(9)]}
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                
                # check row
                if board[i][j] in table["rows"][i]:
                    return False
                table["rows"][i].add(board[i][j])
                
                # check column
                if board[i][j] in table["columns"][j]:
                    return False
                table["columns"][j].add(board[i][j])
                
                # check squre
                k = 3 * (i / 3) + (j / 3)
                if board[i][j] in table["squares"][k]:
                    return False
                table["squares"][k].add(board[i][j])
                
        return True