#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxprofit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                maxprofit += (prices[i+1]-prices[i])
        return maxprofit
        

