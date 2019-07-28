#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        answer = []
        combination = []
        
        def search(candidates, start, target):
            # 2. constraint
            if target == 0:
                # 3. goal
                answer.append(combination[:])
                return
            
            if target < 0:
                return
            
            # 1. choice
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                combination.append(candidates[i])
                search(candidates, i+1, target-candidates[i])
                combination.pop()
        
        search(candidates, 0, target)
        return answer
        

