#
# @lc app=leetcode id=506 lang=python3
#
# [506] Relative Ranks
#
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:

        if not nums:
            return nums
        
        ranks = sorted([(num,i) for i, num in enumerate(nums)], reverse=True)
        answer = [0]*len(nums)
        
        counter = 1
        for score,ind in ranks:
            if counter == 1:
                answer[ind] = "Gold Medal"
            elif counter == 2:
                answer[ind] = "Silver Medal"
            elif counter == 3:
                answer[ind] = "Bronze Medal"
            else:
                answer[ind] = str(counter)
            counter += 1
        
        return answer
        

