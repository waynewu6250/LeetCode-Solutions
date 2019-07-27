class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Find factor less than sqrt(n)
        def isPrime(n):
            if n <= 1:
                return False
            j = 2
            while j*j <= n:
                if n % j == 0:
                    return False
                j += 1
            return True
        
        count = 0
        for i in range(1,n):
            if isPrime(i):
                count += 1
        return count
    
        
        # Use an array to remove multiples
        count, sieve = 0, [True] * n
        for i in range(2, n):
            if sieve[i]:
                count+=1
                for j in range(i*i, n, i):
                    sieve[j] = False
        return count