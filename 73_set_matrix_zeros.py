class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # O(m+n) space
        m = len(matrix)
        n = len(matrix[0])
        array = [0]*(m+n)
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    array[i] = 1
                    array[m+j] = 1
        
        for i in range(len(array)):
            if array[i] == 1:
                if i < m:
                    matrix[i] = [0]*n
                else:
                    for j in range(m):
                        matrix[j][i-m] = 0