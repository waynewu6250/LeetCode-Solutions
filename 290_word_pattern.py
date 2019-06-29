class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        
        str_list = str.split(" ")
        
        if len(pattern) != len(str_list):
            return False
        
        
        pattern_check = dict()
        str_check = dict()
        for i in range(len(pattern)):
            p = pattern[i]
            s = str_list[i]
            
            # Check pattern: string exists
            if pattern_check.get(p, 0) != 0:
                if s != pattern_check[p]:
                    return False
            
            # Check pattern
            if str_check.get(s, 0) != 0:
                if p != str_check[s]:
                    return False
            
            pattern_check[p] = s
            str_check[s] = p
            
        return True