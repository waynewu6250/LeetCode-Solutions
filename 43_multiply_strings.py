class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def convert(string):
            number = 0
            for i,char in enumerate(string[::-1]):
                number += (10**i)*(ord(char)-ord('0'))
            return number
                
        return str(convert(num1)*convert(num2))