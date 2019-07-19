class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        n = 1
        square = 0
        while square <= num:
            square = n ** 2
            if square == num:
                return True
            n += 1
        return False