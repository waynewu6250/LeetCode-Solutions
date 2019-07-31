#
# @lc app=leetcode id=989 lang=python3
#
# [989] Add to Array-Form of Integer
#
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        
        array = ""
        for i in A:
            array += str(i)
        return [int(i) for i in str(int(array)+K)]

