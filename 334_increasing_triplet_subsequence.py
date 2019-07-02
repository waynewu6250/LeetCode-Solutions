class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        if len(nums) < 3:
            return False
        
        min1 = float('inf')
        min2 = float('inf')
        
        for i in nums:
            min1 = min(i,min1)
            if min1 < i:
                min2 = min(i,min2)
            if min2 < i:
                return True
        return False
                