#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        
        
        if not matrix or not matrix[0]:
            return []
        
        answer = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                flag = [0, 0]
                self.bfs(matrix, i, j, flag)
                if flag[0] == 1 and flag[1] == 1:
                    answer.append([i, j])
        return answer
    
    def bfs(self, matrix, i, j, flag):
        
        queue = deque([(i, j)])
        visited = set((i,j))
        
        while queue:
            x, y = queue.popleft()
            
            for x_inc, y_inc in [(0,1), (0,-1), (1,0), (-1,0)]:
                x_new = x + x_inc
                y_new = y + y_inc
                
                if 0 <= x_new < len(matrix) \
                    and 0 <= y_new < len(matrix[0]) \
                    and matrix[x_new][y_new] <= matrix[x][y] \
                    and (x_new,y_new) not in visited:
                    queue.append((x_new, y_new))
                    visited.add((x_new, y_new))
                
                elif x_new < 0 or y_new < 0:
                    flag[0] = 1
                
                elif x_new == len(matrix) or y_new == len(matrix[0]):
                    flag[1] = 1
                    
        
# @lc code=end

