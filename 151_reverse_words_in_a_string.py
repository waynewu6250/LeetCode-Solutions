class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join([str(i) for i in s.split(" ") if str(i) != ''][::-1])