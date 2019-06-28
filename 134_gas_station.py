class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # i is the flag
        i = 0
        while i < len(gas):
            cum = 0
            j = i
            
            # j is the runner
            while True:
                cum += (gas[j] - cost[j])
                j = (j+1) % len(gas)
                if cum < 0:
                    break
                
                # Make a round
                if i == j:
                    return j
            
            if j <= i:
                return -1
            i = j
            