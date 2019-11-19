class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # method 1
        answer = []
        items = []
        def finding_ans(array, items):
           
            if len(array) == 1:
                answer.append(items+array)
                return
            
            for i in range(len(array)):
                finding_ans(array[:i] + array[i+1:], items + [array[i]])
        
        finding_ans(nums, items)
        return answer

        # method 2
        answer = []
        items = []
        visited = [0] * len(nums)
        
        def dfs(items):
            if len(items) == len(nums):
                answer.append(items[:])
            for i in range(len(nums)):
                if visited[i]:
                    continue
                items.append(nums[i])
                visited[i] = 1
                dfs(items)
                items.pop()
                visited[i] = 0
        dfs(items)
        return answer
        