class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len([i for i in s.split(" ") if i != ""]) if s != "" else 0