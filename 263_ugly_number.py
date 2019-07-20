class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        
        def check(num, n):
            while num % n == 0:
                num /= n
            return num
        
        if check(check(check(num,2),3),5) == 1:
            return True
        else:
            return False