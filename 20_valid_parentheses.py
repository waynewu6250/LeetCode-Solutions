class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        
        stack = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            else:
                if not stack:
                    return False
                prev = stack.pop(-1)
                if prev == "(" and s[i] != ")" or \
                   prev == "[" and s[i] != "]" or \
                   prev == "{" and s[i] != "}":
                    return False
                
        if not stack:
            return True
        else:
            return False