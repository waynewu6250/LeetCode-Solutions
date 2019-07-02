class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) <= 1:
            return len(nums)
        
        start = float('inf')
        maxcounter = 1
        counter = 1
        
        for i in sorted(nums):
            
            start = min(i, start)
            if i == start+counter:
                counter += 1
                maxcounter = max(counter, maxcounter)
            if i > start+counter:
                counter = 1
                start = i
            
        return maxcounter