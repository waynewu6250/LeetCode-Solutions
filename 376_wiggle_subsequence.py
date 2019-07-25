class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        if n == 0:
            return 0
        
        up = [0]*n
        down = [0]*n
        
        # 1. Normal dp
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    up[i] = max(up[i],down[j]+1)
                elif nums[j] > nums[i]:
                    down[i] = max(down[i],up[j]+1)
        return 1 + max(down[n-1], up[n-1])
        
        # 2. linear dp: Use current previous stuff directly
        up[0] = 1
        down[0] = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]: #原本是down的就可以加1
                up[i] = down[i-1]+1
                down[i] = down[i-1]
            elif nums[i] < nums[i-1]: #原本是up的就可以加1
                down[i] = up[i-1]+1
                up[i] = up[i-1]
            else:
                up[i] = up[i-1]
                down[i] = down[i-1]
        return max(up[n-1], down[n-1])
    
        # 3. space 1 dp: Use up, down to replace up[i-1], down[i-1]
        up = 1
        down = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]: #原本是down的就可以加1
                up = down+1
            elif nums[i] < nums[i-1]: #原本是up的就可以加1
                down = up+1
        return max(up, down)