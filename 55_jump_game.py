class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # 1. backtracking (Recursive)
        # time complexity: O(2^n)
        # space complexity: O(n)
        def backtracking(nums):

            final = len(nums)-1
            def jump(nums, pos):
                if pos == final:
                    return True
                longest_jumps = min(pos+nums[pos],final)
                for i in range(pos+1,longest_jumps+1):
                    if jump(nums, i):
                        return True
                return False
            
            return jump(nums,0)

        # 2. DP (Top-Down): Store indexes
        # time complexity: O(n^2)
        # space complexity: O(2n)=O(n)
        def top_down(nums):
            final = len(nums)-1
            memo = ["UNKNOWN"] * len(nums)
            
            def jump(nums, pos):
                if memo[pos] != "UNKNOWN":
                    return True if memo[pos] == "GOOD" else False
                
                longest_jumps = min(pos+nums[pos],final)
                for i in range(pos+1,longest_jumps+1):
                    if jump(nums, i):
                        memo[pos] = "GOOD"
                        return True
                
                memo[pos] = "BAD"
                return False
            
            memo[-1] = "GOOD"
            return jump(nums,0)


        # 3. DP (Bottom-Up):
        # time complexity: O(n^2)
        # space complexity: O(2n)=O(n)
        def bottom_up(nums):
            final = len(nums)-1
            memo = ["UNKNOWN"] * final + ["GOOD"]
            
            for i in range(final-1,-1,-1):
                longest_jumps = min(i+nums[i],final)
                
                for j in range(i+1,longest_jumps+1):
                    if memo[j] == "GOOD":
                        memo[i] = "GOOD"
                        break
            
            return memo[0] == "GOOD"
        
        
        # 4. Greedy-search:
        # time complexity: O(n)
        # space complexity: O(1)
        def greedy_search(nums):
            # 1) back to front
            final = len(nums)-1
            leftmost = final
            for i in range(final-1,-1,-1):
                # You will definitely make to leftmost point
                if i+nums[i] >= leftmost:
                    leftmost = i
            return leftmost == 0

            # 2) front to back
            v = nums[0]
            for i in range(1,len(nums)):
                v -= 1
                if v < 0:
                    return False
                if v < nums[i]:
                    v = nums[i]
            return True


        
            # max_ix = 0 
            # for i,item in enumerate(nums):
            #     if i <= max_ix:
            #         if i + item > max_ix:
            #             max_ix = i + item
            #     else:
            #         break
            # return max_ix >= len(nums) - 1