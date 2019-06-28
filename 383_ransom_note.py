class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
#         def count(str):
#             dic = {}
#             for i in str:
#                 dic[i] = dic.get(i,0)+1
#             return dic
        
#         search = count(ransomNote)
#         base = count(magazine)
        
#         for key in count(ransomNote).keys():
#             if key not in base:
#                 return False
#             elif search[key] > base[key]:
#                 return False
#         return True

        def count(str):
            dic = {}
            for i in str:
                dic[i] = dic.get(i,0)+1
            return dic
        
        base = count(magazine)
        
        for i in ransomNote:
            if i not in base:
                return False
            else:
                base[i] = base[i]-1
                if base[i] < 0:
                    return False
        return True