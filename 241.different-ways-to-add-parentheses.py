#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#
class Solution:

    def diffWaysToCompute(self, input):
        if input.isdigit():
            return [int(input)]
        ans = []
        for i in range(len(input)):
            if input[i] in "-+*":
                ans1 = self.diffWaysToCompute(input[:i])
                ans2 = self.diffWaysToCompute(input[i+1:])
                for j in ans1:
                    for k in ans2:
                        ans.append(self.helper(j, k, input[i]))
        return ans

    def helper(self, m, n, op):
        if op == "+":
            return m+n
        elif op == "-":
            return m-n
        else:
            return m*n
        

