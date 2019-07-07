class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        product = 1
        product_without_zeros = 1
        if len([0 for i in nums if i == 0]) >= 2:
            return [0]*len(nums)
        
        for i in nums:
            product *= i
            if i != 0:
                product_without_zeros *= i
        for i in nums:
            if i == 0:
                answer.append(product_without_zeros)
            else:
                answer.append(product / i)
        return answer