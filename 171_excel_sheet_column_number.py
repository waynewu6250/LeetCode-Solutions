class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        dic = {character: i+1 for i, character in enumerate(characters)}
        
        ans = 0
        for i,vocab in enumerate(s[::-1]):
            ans += dic[vocab] * (26**i)
        return ans