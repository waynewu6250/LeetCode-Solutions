# 1.一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
# 2.我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
import time

def timing(func):
    def wraps(*args):
        start = time.time()
        func(*args)
        print("time is: %.8f s"%((time.time()-start)))
    return wraps


n = input("Please insert n: ")
n = int(n)

# Recursion solution
@timing
def func1(n):
    fib = lambda n: n if n <= 2 else fib(n-1)+fib(n-2)
    print("Solution 1 is: ",fib(n))


# Dynamic programming solution + decorator
@timing
def func2(n):
    def store(func):
        cache = {}
        def wraps(*args):
            if args not in cache:
                cache[args] = func(*args)
            return cache[args]
        return wraps

    @store
    def func(n):
        if n<=2:
            return n
        return func(n-1)+func(n-2)
    print("Solution 2 is: ",func(n))

# Iteration
@timing
def func3(n):
    def fib2(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return b
    print("Solution 3 is: ",fib2(n))

func1(n)
func2(n)
func3(n)


#一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
@timing
def func4(n):
    fib = lambda n: n if n <= 2 else 2*fib(n-1)
    print("Solution for second problem is: ",fib(n))
func4(n)



