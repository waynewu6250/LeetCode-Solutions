#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        cache = {}
        for i in s:
            cache[i] = cache.get(i,0) + 1
        
        length = 0
        single = False
        for k,v in cache.items():
            if v % 2 == 0:
                length += v
            elif v > 2:
                length += (v-1)
                single = True
            else:
                single = True
            
        
        return length+1 if single else length
        
# @lc code=end

