#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = {}
        for i in nums:
            dic[i] = dic.get(i,0)+1
        dic = sorted(dic.items(), key = lambda x: x[1], reverse=True)
        return [x for x, y in dic[:k]]
        

