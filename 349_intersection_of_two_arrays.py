class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #return [i for i in set(nums1) if i in set(nums2)]
        
        pair = (nums1,nums2) if len(nums1) > len(nums2) else (nums2,nums1)
        big, small = pair
        small = set(small)
        big = sorted(big)
        
        ans = []
        for i in small:
            
            left = 0
            right = len(big)-1
            while left <= right:
                mid = (left+right) // 2
                if i == big[mid]:
                    ans.append(i)
                    break
                elif i < big[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return ans