#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        dic = {}
        for i in words:
            dic[i] = dic.get(i, 0) + 1
        dic = sorted(dic.items(), key = lambda x: (-x[1], x[0]))
        return [i[0] for i in dic[:k]]
        
# @lc code=end

