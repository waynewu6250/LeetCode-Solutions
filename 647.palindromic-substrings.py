#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:

        counter = 0
        
        for i in range(len(s)):
            counter = self.ispa(s, i, i, counter)
            counter = self.ispa(s, i, i+1, counter)
        return counter
        
    def ispa(self, s, left, right, counter):
       
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                return counter
            counter += 1
            left -= 1
            right += 1
        
        return counter
        
# @lc code=end

