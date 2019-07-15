class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        left = 0
        right = 0
        length = 0
        cache = {}
        
        while right < len(s):
            if s[right] in cache and cache[s[right]] >= left:
                left = cache[s[right]] + 1
            else:
                cache[s[right]] = right
                right += 1
                
            if right-left > length:
                length = right-left
            
        return length