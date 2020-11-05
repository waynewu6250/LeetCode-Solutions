#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#

# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:

        num = list(str(num))
        for i in range(len(num)):
            j = self.check(num, i)
            if num[j] != num[i]:
                swap = num[i]
                num[i] = num[j]
                num[j] = swap
                return int(''.join(num))
        return int(''.join(num))
    
    def check(self, num, i):
        maximum = int(num[i])
        max_id = i
        for j in range(i+1, len(num)):
            if int(num[j]) >= maximum:
                maximum = int(num[j])
                max_id = j
        return max_id
        
        
# @lc code=end

