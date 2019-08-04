#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#
class Solution:
    def convertToBase7(self, num: int) -> str:
        
        answer = ""
        s = ""
        
        if num < 0:
            num = -num
            answer += "-"
        
        while num >= 7:
            s += str(int(num%7))
            num /= 7
        
        s += str(int(num%7))
        return answer+s[::-1]
        

