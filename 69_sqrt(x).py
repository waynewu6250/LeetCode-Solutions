class Solution:
    def mySqrt(self, x: int) -> int:
        
        for i in range(x+1):
            
            count = i * i
            if count < x:
                continue
            else:
                if count == x:
                    return i
                else:
                    return i - 1