class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        # 1. Use a list to store the value you've seen at which index
        nxt = [float('inf')] * 102
        ans = [0]*len(T)
        
        for i in xrange(len(T)-1,-1,-1):
            # check warmer index, if have one then put it in answer
            warmer_index = min([nxt[t] for t in xrange(T[i]+1,102)])
            if warmer_index < float('inf'):
                ans[i] = warmer_index - i
            
            # put what you have seen
            nxt[T[i]] = i
        
        return ans
            
        # 2. Use stack to store the value decrease
        stack = []
        ans = [0]*len(T)
        
        for i in xrange(len(T)-1,-1,-1):
            
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            
            stack.append(i)
        return ans