#
# @lc app=leetcode id=1189 lang=python3
#
# [1189] Maximum Number of Balloons
#

# @lc code=start
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        cache = {}
        for t in text:
            cache[t] = cache.get(t,0) + 1
        
        match = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
        
        counter = []
        for k, v in cache.items():
            if k in match:
                counter.append(cache[k] // match[k])
        if len(counter) == 5:
            return min(counter)
        else:
            return 0
        
# @lc code=end

