class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        answer = []
        items = []
        
        def backtrack(items, start, target):
            if target == 0:
                answer.append(items)
                return
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                backtrack(items+[candidates[i]], i, target-candidates[i])
        
        backtrack(items, 0, target)
        return answer