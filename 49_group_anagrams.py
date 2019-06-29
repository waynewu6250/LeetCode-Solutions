class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = {}
        for i in strs:
            key = tuple(sorted(i))
            dic[key] = dic.get(key,[])+[i]
        
        return [v for v in dic.values()]