class Solution(object):
    
    
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        subset = []
        
        # solution 1
        def get_subsets(nums, start, answer, subset):
            
            answer.append(subset[:])
            for i in range(start,len(nums)):
                subset.append(nums[i])
                get_subsets(nums, i+1, answer, subset)
                subset.pop()
        
        # solution 2
        def get_subsets(nums, start, answer, subset):

            if start == len(nums)-1:
                answer.append(subset[:])
            else:
                subset.append(nums[i])
                get_subsets(nums, i+1, answer, subset)
                subset.pop()
                get_subsets(nums, i+1, answer, subset)
        
        get_subsets(nums, 0, answer, subset)
        return answer

