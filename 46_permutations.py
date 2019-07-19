class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def finding_ans(array, temp):
            if len(array) == 1:
                ans.append(temp+array)
                return
            for i in range(len(array)):
                finding_ans(array[:i] + array[i+1:], temp + [array[i]])
        finding_ans(nums, [])
        return ans