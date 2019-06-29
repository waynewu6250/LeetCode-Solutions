class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        h = 0
        for i, c in enumerate(sorted(citations)[::-1]):
            if c >= i+1:
                h = i+1
        return h  