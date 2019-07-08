class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # 1. Sorting
        nums1[:] = nums1[:m] + nums2
        nums1.sort()
        
        # 2. Non-sorting
        for i in range(m,len(nums1)):
            nums1[i] = nums2[i-m]
        
        for i in range(m+n):
            value = nums1[i]
            f = i-1
            while f>=0:
                if value < nums1[f]:
                    temp = nums1[f]
                    nums1[f] = value
                    nums1[f+1] = temp
                    f-=1
                else:
                    break