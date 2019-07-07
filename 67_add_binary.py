class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = [int(i) for i in a[::-1]]
        b = [int(j) for j in b[::-1]]
        pair = (a,b) if len(a) < len(b) else (b,a)
        (small, big) = pair
        small += [0]*(abs(len(a)-len(b)))
        
        carry = 0
        ans = ""
        for i,j in zip(small,big):
            
            mod = (i + j + carry) % 2
            carry = (i + j + carry) / 2
            ans += str(mod)
        if carry != 0:
            ans += str(carry)
        
        return ans[::-1]