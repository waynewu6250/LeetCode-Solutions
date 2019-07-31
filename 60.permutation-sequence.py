#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 1. backtracking
        # answer = []
        # items = ""
        # nums = list(range(1,n+1))
        
        # def backtrack(items, array):
            
        #     if len(array) == 1:
        #         answer.append(items+str(array[0]))
            
        #     for i in range(len(array)):
                
        #         backtrack(items+str(array[i]),array[:i]+array[i+1:])
        
        # backtrack(items, nums)
        # return answer[k-1]
    
        # 2. find pattern
        num = "123456789";
        f = [1]*n
        res = ""
        
        # set up n!
        for i in range(1,n):
            f[i] = f[i-1] * i
        
        k-=1
        for i in range(n,0,-1):
            j = k//f[i-1]
            k %= f[i-1]
            res += num[j]
            num = num[:j]+num[j+1:]
        return res
        

