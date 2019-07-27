class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # farthest we can reach
        farthest = 0
        # current where we stand
        cur = 0
        # how many step we use
        steps = 0
        
        i = 0
        while i < n:
            # Reach the end
            if cur >= n-1:
                break
            
            # Start to choose
            while i <= cur:
                farthest = max(farthest, nums[i]+i)
                i+=1
            
            # update our position and add 1 to steps
            steps += 1
            cur = farthest
                
        return steps