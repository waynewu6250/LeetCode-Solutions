#
# @lc app=leetcode id=292 lang=python3
#
# [292] Nim Game
#
class Solution:
    def canWinNim(self, n: int) -> bool:
        return not ((n % 4) == 0)
        

