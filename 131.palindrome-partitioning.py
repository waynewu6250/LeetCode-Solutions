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
        
######################################################
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        answer = []
        items = []
        self.dfs(answer, items, 0, s)
        return answer
    
    def dfs(self, answer, items, start, s):
        
        print(start)
        
        if start == len(s):
            answer.append(items)
        
        for i in range(start, len(s)):
            if self.is_palindrome(s, start, i):
                self.dfs(answer, items + [s[start:i+1]], i+1, s)
            
    
    def is_palindrome(self, s, i, j):
        
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True