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
        
        # m1: the number of list1 to take
        # m2: the number of list2 to take
        # k: the total number to take
        
        
        len1 = len(nums1)
        len2 = len(nums2)
        left = 0
        right = len1
        k = (len1+len2+1) // 2
        
        while left <= right:
            
            m1 = (left+right) // 2
            m2 = k - m1
            
            leftX = nums1[m1-1] if m1 > 0 else -float('inf')
            rightX = nums1[m1] if m1 != len1 else float('inf')
            leftY = nums2[m2-1] if m2 > 0 else -float('inf')
            rightY = nums2[m2] if m2 != len2 else float('inf')
            
            # correct partition point
            if leftX <= rightY and rightX >= leftY:
                if (len1+len2) % 2 == 0:
                    return (max(leftX, leftY) + min(rightX, rightY)) / 2.0
                else:
                    return max(leftX, leftY)
            
            # Not correct partition point
            elif leftX > rightY:
                right = m1 - 1
            else:
                left = m1 + 1

