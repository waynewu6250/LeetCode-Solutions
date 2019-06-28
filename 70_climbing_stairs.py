class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def memo(func):
            cache = {}
            def wraps(*args):
                if args not in cache:
                    cache[args] = func(args)
                return cache[args]
            return wraps
        
        @memo
        def climb(nn):
            nn = nn[0] #nn=(n,), get the first one
            if nn <= 2:
                return nn
            return climb(nn-1)+climb(nn-2)
        
        return climb(n)