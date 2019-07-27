class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # 1. Use O(n) space: array or heap
        return sorted([num for row in matrix for num in row])[k-1]
        
        # 2. binary search
        # https://www.cnblogs.com/grandyang/p/5727892.html