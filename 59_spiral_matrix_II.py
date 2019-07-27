class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def indexes(r1,r2,c1,c2):
            for c in range(c1, c2+1):
                yield r1, c
            for r in range(r1+1,r2+1):
                yield r, c2
            
            if r1 < r2 and c1 < c2: #important
                for c in range(c2-1, c1, -1):
                    yield r2, c
                for r in range(r2, r1, -1):
                    yield r, c1
                
        array = [[0]*n for _ in range(n)]
        
        c1, c2 = 0, n-1
        r1, r2 = 0, n-1
        
        counter = 1
        while r1 <= r2 and c1 <= c2:
            for r, c in indexes(r1,r2,c1,c2):
                array[r][c] = counter
                counter += 1
            r1 += 1
            r2 -= 1
            c1 += 1
            c2 -= 1
        return array