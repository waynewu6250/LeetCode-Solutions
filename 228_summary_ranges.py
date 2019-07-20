class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return ""
        
        left = 0
        right = 1
        answer = []
        
        while right <= len(nums):
            
            if right == len(nums) or nums[right] != nums[right-1]+1:
                ans = str(nums[left]) if left == right-1 else str(nums[left])+"->"+str(nums[right-1])
                answer.append(ans)
                left = right
            right += 1
        
        return answer