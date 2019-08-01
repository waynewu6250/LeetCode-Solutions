#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        self.array = sorted(nums)
        self.k = k
        

    def add(self, val: int) -> int:
        
        start = 0
        end = len(self.array)-1
        
        while start <= end:
            mid = (start+end) // 2
            if self.array[mid] >= val:
                end = mid-1
            else:
                start = mid+1
        self.array.insert(start,val)
        return self.array[len(self.array)-self.k]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

