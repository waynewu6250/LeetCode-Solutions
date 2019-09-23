#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answers = []
        items = ""
        
        def recur(items, left, right):
            
            if len(items) == 2*n:
                answers.append(items)
                return
            if left < n:
                recur(items+"(", left+1, right)
            if right < left:
                recur(items+")", left, right+1)
        
        recur(items, 0, 0)
        return answers
        

