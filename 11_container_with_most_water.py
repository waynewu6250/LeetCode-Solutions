class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # 1. brute force
        # maxarea = 0
        # for i in range(len(height)):
        #     for j in range(i, len(height)):
        #         if (j-i)*min(height[j],height[i]) > maxarea:
        #             maxarea = (j-i)*min(height[j],height[i])
        # return maxarea
        
        # 2. Two pointer (head, tail)
        front = 0
        end = len(height)-1
        maxarea = 0
        
        while front < end:
            
            minimum = min(height[front],height[end])
            if (end-front) * minimum > maxarea:
                maxarea = (end-front) * minimum
            if height[front] < height[end]:
                front += 1
            else:
                end -= 1
        
        return maxarea