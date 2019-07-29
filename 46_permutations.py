class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
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