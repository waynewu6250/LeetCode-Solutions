class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        answer = []
        intervals = sorted(intervals, key = lambda x: x[0])
        
        for interval in intervals:
            if not answer or answer[-1][-1] < interval[0]:
                answer.append(interval)
            else:
                answer[-1][-1] = max(answer[-1][-1], interval[-1])
                
        return answer