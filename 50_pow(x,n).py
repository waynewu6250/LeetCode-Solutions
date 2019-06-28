class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def memo(func):
            cache = {}
            def wraps(*args):
                if args not in cache:
                    cache[args] = func(*args)
                return cache[args]
            return wraps
        
        @memo
        def power(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            
            f = n // 2
            c = n-f
            return power(x, c) * power(x, f)
        
        if n < 0:
            return 1 / power(x,abs(n))
        else:
            return power(x, n)