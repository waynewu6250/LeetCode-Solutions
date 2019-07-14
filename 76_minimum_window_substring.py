class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        cache = {}
        for i in t:
            cache[i] = cache.get(i,0)+1
        
        left = 0
        right = 0
        counter = len(cache)
        ans = ''
        length = float('inf')

        while right < len(s):
            
            # 1. Move right pointer to meet requirement
            if s[right] in cache:
                cache[s[right]] = cache[s[right]]-1
                if cache[s[right]] == 0:
                    counter -= 1
            
            right += 1
            
            
            while counter == 0:
                # 2. When meeting requirement, check goal
                if right-left < length:
                    length = right-left
                    ans = s[left:right]
                
                # 4. If reaching the character in t, move right again
                if s[left] in cache:
                    cache[s[left]] = cache[s[left]]+1
                    if cache[s[left]] > 0:
                        counter += 1
                
                # 3. Try to shorten the length
                left += 1
        
        return ans
                