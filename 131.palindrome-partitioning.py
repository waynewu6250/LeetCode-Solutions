#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
class Solution:
    def partition(self, s: str) -> List[List[str]]:

        answer = []
        items = []
        def isPalindrome(start, end):
            while start < end:
                if s[start] == s[end]:
                    start+=1
                    end-=1
                else:
                    return False
            return True
        
        def backtrack(items, start):
            
            if start == len(s):
                answer.append(items)
                return
            
            for i in range(start,len(s)):
                if isPalindrome(start, i):
                    backtrack(items+[s[start:i+1]], i+1)
        
        backtrack(items, 0)
        return answer
        

