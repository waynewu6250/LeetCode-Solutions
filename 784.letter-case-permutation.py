#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        answer = []
        items = ""
        
        def backtrack(items, start):
            
            if start == len(S):
                answer.append(items)
                return
            
            if S[start].upper() == S[start].lower():
                backtrack(items+S[start], start+1)
            else:
                backtrack(items+S[start].upper(), start+1)
                backtrack(items+S[start].lower(), start+1)
        
        backtrack(items, 0)
        return answer
        

