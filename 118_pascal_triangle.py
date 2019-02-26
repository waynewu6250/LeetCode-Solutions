class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        def memo(func):
            cache = {}
            def wraps(*args):
                if args not in cache:
                    cache[args] = func(*args)
                return cache[args]
            return wraps
        
        @memo
        def pascal(n,k):
            if n == 0: return 0
            if k == 0: return 1
            return pascal(n-1,k)+pascal(n-1,k-1)
        
        ans = []
        for i in range(1,numRows+1):
            row = []
            for j in range(i):
                row.append(pascal(i,j))
            ans.append(row)
        return ans