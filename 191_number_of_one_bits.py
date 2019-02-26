class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = bin(n)[2:]
        string = '0'*(32-len(binary))+binary
        count = 0
        for i in string:
            if int(i) | 0:
                count+=1
        return count