class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        counter = 0
        prev = -1
        for i in range(len(s)):
            # 1. Satisfy the condition
            if (prev == "I" and (s[i] == "V" or s[i] == "X")) or \
               (prev == "X" and (s[i] == "L" or s[i] == "C")) or \
               (prev == "C" and (s[i] == "D" or s[i] == "M")):
                counter += (dic[s[i]]-dic[prev])
                prev = -1
            else:
                # 2. we have value for prev
                if prev != -1:
                    counter += dic[prev]
                # 3. we don't have value for prev
                prev = s[i]
                if i == len(s)-1:
                    counter += dic[s[i]]
                
        return counter