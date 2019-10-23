#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def is_palindrome(s, i, j):
            
            while i <= j:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1
            return True
        
        answer = []
        items = []
        
        def recur(items, start):
            
            if start == len(s):
                answer.append(items)
            
            for i in range(start, len(s)):
                if is_palindrome(s, start, i):
                    recur(items+[s[start:i+1]], i+1)
        
        recur(items, 0)
        return answer
        

