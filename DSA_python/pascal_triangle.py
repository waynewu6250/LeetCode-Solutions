# 1. dynamic programming: top-down method
def memo(func):
    
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memo
def pascal_v1(n,k):
    if k==0: return 1
    if n==0: return 0
    return pascal_v1(n-1,k-1)+pascal_v1(n-1,k)


# 2. dynamic programming: bottom-up method
from collections import defaultdict
def pascal_v2(n,k):
    cache = defaultdict(int)
    for i in range(n+1):
        cache[i,0] = 1
        for j in range(1,k+1):
            cache[i,j] = cache[i-1,j-1]+cache[i-1,j]
    return cache[n,k]


if __name__ == "__main__":  
    print(pascal_v1(8,5))
    print(pascal_v2(8,5))