class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        answer = ""
        after_repeat = ""
        repeat = ""
        stack = []
        number = ""
        
        for i in range(len(s)+1):
            if stack and stack[-1] == "]":
                
                # Get number and repeat chr
                stack.pop()
                while stack[-1] != "[":
                    repeat += stack.pop()
                stack.pop()
                
                while stack and ord(stack[-1]) - ord('0') < 10:
                    number += stack.pop()
                
                number = int(number[::-1])
                
                # answer adding
                while number > 0:
                    after_repeat += repeat[::-1]
                    number -= 1
                
                if stack:
                    for char in after_repeat:
                        stack.append(char)
                else:
                    answer += after_repeat
                
                repeat = ""
                after_repeat = ""
                number = ""
            
            if i != len(s):
                stack.append(s[i])
        
        last = ""
        while stack:
            last += stack.pop()
        return answer+last[::-1]