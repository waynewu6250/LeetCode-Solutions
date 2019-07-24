class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Method 1: top-down
        def memo(func):
            cache = {}
            def wraps(*args):
                if args not in cache:
                    cache[args] = func(*args)
                return cache[args]
            return wraps
        
        @memo
        def climb(nn):
            nn = nn[0] #nn=(n,), get the first one
            if nn <= 2:
                return nn
            return climb(nn-1)+climb(nn-2)
        
        return climb(n)
        
        # Method 2: bottom-up
        dp = [1]*(n+1)
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        
        # Method 3: bottom-up optimization
        dp1, dp2 = 1, 1
        for i in range(2, n+1):
            dp2, dp1, = dp1+dp2, dp2
        return dp2

        