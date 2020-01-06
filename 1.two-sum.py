#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # front-back
        # dic = [(num, i) for i, num in enumerate(nums)]
        # dic = sorted(dic, key = lambda x: x[0])
        
        # left = 0 
        # right = len(dic)-1
        # while left < right:
        #     if dic[left][0]+dic[right][0] > target:
        #         right-=1
        #     elif dic[left][0]+dic[right][0] < target:
        #         left+=1
        #     else:
        #         return [dic[left][1], dic[right][1]]


        # minus
        
        # hashtable
        dic = {num: i for i, num in enumerate(nums)}
        
        for i, num in enumerate(nums):
            if (target-num) in dic and i != dic[target-num]:
                return [i, dic[target-num]]

        

