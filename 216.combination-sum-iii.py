#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        candidates = range(1,10)
        combination = []
        answer = []
        
        def search(combination, start, target):
            
            if len(combination) == k and target == 0:
                answer.append(combination[:])
                return 
            
            if len(combination) > k or target < 0:
                return
            
            for i in range(start, len(candidates)):
                search(combination+[candidates[i]], i+1, target-candidates[i])
        
        search(combination, 0, n)
        return answer
        

