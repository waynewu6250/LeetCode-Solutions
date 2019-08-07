#
# @lc app=leetcode id=868 lang=python3
#
# [868] Binary Gap
#
class Solution:
    def binaryGap(self, N: int) -> int:

        s = ""
        while N >= 2:
            s += str(int(N % 2))
            N /= 2
        s += str(int(N % 2))
        s = s[::-1]
        
        longest = 0
        length = 1
        start = 0
        end = 1
        while end != len(s):
            if int(s[start])*int(s[end]) == 1:
                longest = max(end-start, longest)
                length = 0
                start = end
            length += 1
            end += 1
        
        return longest
        

