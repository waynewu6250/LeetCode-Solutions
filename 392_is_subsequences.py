class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':
            return True
        
        ptr1 = len(s)-1
        ptr2 = len(t)-1
        while ptr1 >= 0 and ptr2 >= 0:
            if s[ptr1] == t[ptr2]:
                ptr1-=1
                ptr2-=1
            else:
                ptr2-=1
        
        if ptr1 == -1:
            return True
        else:
            return False