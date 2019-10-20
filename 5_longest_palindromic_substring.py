class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # Brute force
        def is_palindrome(s, i , j):
            while i <= j:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1
            return True
        
        n = len(s)
        start = 0
        length = 1
        
        for i in range(n):
            for j in range(i,n):
                if is_palindrome(s, i, j) and j-i+1 > length:
                    start = i
                    length = j-i+1
        return s[start:start+length]

        ########################################################
        # dp method
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        
        start = 0
        maxlen = 1
        
        # initialization
        for i in range(n):
            dp[i][i] = 1
            if i < n-1 and (s[i] == s[i+1]):
                dp[i][i+1] = 1
                start = i
                maxlen = 2
        
        # run
        for i in range(n-1,-1,-1):
            for j in range(i+2,n):
                if dp[i+1][j-1] and (s[i] == s[j]):
                    dp[i][j] = 1
                    if (j-i >= maxlen):
                        start = i
                        maxlen = j-i+1
        
        return s[start:start+maxlen]