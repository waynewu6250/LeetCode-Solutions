#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # nums1 shorter, nums2 longer
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        
        len1 = len(nums1)
        len2 = len(nums2)
        left = 0
        right = len1
        
        while left <= right:
            
            partitionX = (left+right) // 2
            partitionY = (len1+len2+1) // 2 - partitionX
            
            leftX = nums1[partitionX-1] if partitionX > 0 else -float('inf')
            rightX = nums1[partitionX] if partitionX != len1 else float('inf')
            leftY = nums2[partitionY-1] if partitionY > 0 else -float('inf')
            rightY = nums2[partitionY] if partitionY != len2 else float('inf')
            
            # Right partition point
            if leftX <= rightY and rightX >= leftY:
                if (len1+len2) % 2 == 0:
                    return (max(leftX, leftY) + min(rightX, rightY)) / 2.0
                else:
                    return max(leftX, leftY)
            
            # Not right point
            elif leftX > rightY:
                right = partitionX - 1
            else:
                left = partitionX + 1

