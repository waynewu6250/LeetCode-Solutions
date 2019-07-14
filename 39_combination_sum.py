class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
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
                combination.append(candidates[i])
                search(candidates, start, target-candidates[i])
                combination.pop()
        
        search(candidates, 0, target)
        return answer