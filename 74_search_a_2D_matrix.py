class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        def binary_search(array, target):
            left = 0
            right = len(array)-1
            while left <= right:
                mid = (left+right) // 2
                if array[mid] == target:
                    return mid, True
                elif array[mid] < target:
                    left = mid+1
                elif array[mid] > target:
                    right = mid-1
            return right, False 
        
        #matrix = sorted(matrix, key = lambda x: x[0])
        m = [row[0] for row in matrix]
        
        index, _ = binary_search(m, target)
        _, answer = binary_search(matrix[index],target)
        
        return answer