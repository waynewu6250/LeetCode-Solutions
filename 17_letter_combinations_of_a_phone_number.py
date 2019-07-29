class Solution:
    def letterCombinations(self, digits):
        
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
            
        answer = []
        items = ""
        def backtrack(next_digits, items):

            if len(next_digits) == 0:
                answer.append(items)
                return
          
            for letter in phone[next_digits[0]]:
                backtrack(items + letter, next_digits[1:])
                    
        
        if digits:
            backtrack(digits, items)
        return answer