class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1. extra space
        # if len(nums) == 0:
        #     return -1
        # count = range(1,len(nums)+1)
        # for i in nums:
        #     if i not in count:
        #         return i
        #     count.remove(i)
        
        # 2. sorting
        # prev = -1
        # for i in sorted(nums):
        #     if prev == i:
        #         return i
        #     prev = i
        
        # 3. Tortoise and hare
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        ptr1 = nums[0]
        ptr2 = slow
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
            
        return ptr1