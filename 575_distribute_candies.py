class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        # set
        kinds = len(set(candies))
        return min(len(candies)/2,kinds)
    
        # sort
        candies = sorted(candies)
        count = 1
        for i in range(1,len(candies)):
            if candies[i] > candies[i-1] and count < len(candies)/2:
                count += 1
        return count
        