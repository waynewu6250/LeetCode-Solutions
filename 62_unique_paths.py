class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 1. recursive
        def f(x,y):
            if x <=0 or y<=0: return 0
            if x == 1 and y == 1: return 1
            return f(x-1,y)+f(x,y-1)
        return f(m,n)
    
        # 2. top-down
        def memo(func):
            cache = {}
            def wraps(*args):
                if args not in cache:
                    cache[args] = func(*args)
                return cache[args]
            return wraps
        
        @memo
        def f(x,y):
            if x <=0 or y<=0: return 0
            if x == 1 and y == 1: return 1
            return f(x-1,y)+f(x,y-1)
        return f(m,n)

        # 3. bottom-up
        def f(x,y):
            dp = [[0]*(m+1) for _ in range(n+1)]
            dp[1][1] = 1
            for i in range(1, x+1):
                for j in range(1, y+1):
                    if i == 1 and j == 1:
                        continue
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
            return dp[x][y]
        return f(n,m)