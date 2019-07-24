class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        dp = [0]*(len(s)+1)
        for i in range(1,len(s)+1):
            for word in wordDict:
                start = i-len(word)
                if start > -1:
                    if s[start:i] == word and (dp[start] or start == 0):
                        dp[i] = True
                        break
        return dp[-1]