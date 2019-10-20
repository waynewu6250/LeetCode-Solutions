#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        
        # 1. 
#         start = 0
#         end = len(sub)-1
#         while start < end:
#             if sub[start] != sub[end]:
#                 return False
#             start+=1
#             end-=1
#         return True
        
#         for i in range(len(s)):
#             if check(s[:i]+s[i+1:]):
#                 return True
#         return False
            
        # 2. 
        def is_pali_range(i, j):
            return all(s[k] == s[j-k+i] for k in range(i, j))

        start = 0
        end = len(s)-1
        while start < end:
            if s[start] == s[end]:
                start+=1
                end-=1
            else:
                return is_pali_range(start+1,end) or is_pali_range(start,end-1)
        return True
        
# @lc code=end

