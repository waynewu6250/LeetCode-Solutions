class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # 1. Brute Force
        # Time complexity = O(n^2)
        # Space complexity = O(1)
        # maxprofit = 0
        # for i in range(len(prices)-1):
        #     for j in range(i+1,len(prices)):
        #         value = prices[j] - prices[i]
        #         if value > maxprofit:
        #             maxprofit = value
        # return maxprofit
        
        # 2. One pass
        # Time complexity = O(n)
        # Space complexity = O(1)
        if len(prices) == 0:
            return 0
        
        minimum = prices[0]
        maxprofit = 0
        for i in range(1,len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            elif prices[i] - minimum > maxprofit:
                maxprofit = prices[i] - minimum
                
        return maxprofit