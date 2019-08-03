#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#
class Solution:
    
    def minimumTotal3(self, triangle):
        if not triangle:
            return 
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]

    # bottom-up, O(n) space
    def minimumTotal(self, triangle):
        if not triangle:
            return 
        res = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j+1]) + triangle[i][j]
        return res[0]
        

