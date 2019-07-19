class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        
        ans = []
        def find_ans(array, tmp):
            if len(array) == 1:
                ans.append(tmp+array)
                return
            for i in range(len(array)):
                if i > 0 and array[i-1] == array[i]:
                    continue
                find_ans(array[:i]+array[i+1:], tmp+[array[i]])
        find_ans(nums, [])
        
        return ans