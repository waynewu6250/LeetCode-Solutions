class Solution:

    # Recursion
    def memo(func):
        cache = {}
        def wraps(*args):
            if args not in cache:
                cache[args] = func(*args)
            return cache[args]
        return wraps
        
    @memo
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        else:
            return self.fib(N-1)+self.fib(N-2)
    
    # Tail Recursion
    def fib(self, N: int, a, b) -> int:
        if N == 0:
            return a
        else: return fib(N-1, b, a+b)

    
    # Iteration
    a, b = 0, 1
    
    if N == 0:
        return a
    
    for _ in range(N-2):
        prev = a
        a = b
        b = prev + b
    return b
