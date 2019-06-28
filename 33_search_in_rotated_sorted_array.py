class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return -1
        
        minimum = float('inf')
        for i,num in enumerate(nums):
            if num < minimum:
                minimum = num
                index = i
        
        array = nums[index:]+nums[:index]
        indexes = list(range(index,len(nums)))+list(range(index))
        
        start = 0
        end = len(array)-1
        while start <= end:
            mid = int((start+end)/2)
            
            if target == array[mid]:
                return indexes[mid]
            elif target < array[mid]:
                end = mid-1
            elif target > array[mid]:
                start = mid+1
        return -1