class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        # DP bottom up method
        # 1. set up dp array
        n = len(S)
        l =[0]*(n+1)
        r =[0]*(n+1)
        l[0] = ord(S[0]) - ord('0')
        r[n-1] = ord('1') - ord(S[n-1])
        
        # 2. for loop
        for i in range(1,n):
            l[i] = l[i-1] + ord(S[i]) - ord('0')
        for i in range(n-2,-1,-1):
            r[i] = r[i+1] + ord('1') - ord(S[i])
        
        ans = r[0]
        for i in range(1,n+1):
            ans = min(ans, l[i-1]+r[i])
        return ans