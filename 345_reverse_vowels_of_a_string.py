class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 1. iterative+allocate
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        indexes = []
        chars = []
        for i, char in enumerate(s):
            if char in vowels:
                indexes.append(i)
                chars.append(str(char))
        
        ans = ""
        for i in range(len(s)):
            if i not in indexes:
                ans += s[i]
            else:
                ans += chars.pop()
        return ans
    
        # 2. iterative+inplace
        vowels_set = set(['a','e','i','o','u'])
        s = list(s)
        l,r = 0,len(s) - 1
        while l < r:
            if s[l].lower() not in vowels_set:
                l += 1
            elif s[r].lower() not in vowels_set:
                r -= 1
            else:
                s[l],s[r] = s[r],s[l]
                l += 1
                r -= 1
        
        return ''.join(s)