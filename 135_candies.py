class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        candies = [1]*n
        
        # left to right
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1]+1
        
        # right to left
        for i in range(n-2,-1,-1):
            if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
                candies[i] = candies[i+1]+1
        
        return sum(candies)