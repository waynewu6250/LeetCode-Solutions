class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        if len(citations) == 0:
            return 0
        
        n = len(citations)
        start = 0
        end = n-1
        
        while start < end:
            
            mid = (start+end) // 2
            # e.g. We want at least 5 papers, but we only get 2
            if citations[mid] >= n-mid:
                end = mid
                
            # e.g. We want at least 2 papers, and we have more as 5
            else: 
                start = mid+1
        return n - end if (citations[end] >= n - end) else 0