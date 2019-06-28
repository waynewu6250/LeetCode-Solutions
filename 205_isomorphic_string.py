class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def index(string):
            arr = [0]*len(string)
            dic = {}
            counter = 0
            for i in range(len(string)):
                if string[i] not in dic:
                    dic[string[i]] = counter
                arr[i] = dic[string[i]]
                counter += 1
            return arr
            
        if len(s) != len(t):
            return False
        return index(s) == index(t)