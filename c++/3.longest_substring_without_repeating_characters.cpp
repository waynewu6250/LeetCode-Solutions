class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        int left = 0;
        int right = 0;
        int maxlen = 0;
        unordered_map<int, int> cache;
        
        while(right < s.size()){
            if(cache.find(s[right]) != cache.end() && cache[s[right]] >= left){
                left = cache[s[right]] + 1;
                
            }else{
                cache[s[right]] = right;
                right += 1;
            }
            maxlen = max(right-left, maxlen);
        }
        return maxlen;
        
    }
};