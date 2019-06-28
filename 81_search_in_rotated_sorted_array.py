class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False
        
        # Find minimum
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            val = nums[mid]
            if val < nums[end]:
                end = mid
            elif val > nums[end]:
                start = mid + 1
            else:
                if nums[end] < nums[end - 1]: break   ## avoid index equals to 0 in some cases
                end -= 1
        
		#Find which side
        if end == 0:
            start, end = 0, len(nums) - 1
        else:
            start, end = (0, end - 1) if nums[0] <= target else (end, len(nums) - 1)
        
        
        while start <= end:
            mid = (start+end) // 2
            
            if target == nums[mid]:
                return True
            elif target < nums[mid]:
                end = mid-1
            elif target > nums[mid]:
                start = mid+1
        return False