class Solution {
public:
    int rob(vector<int>& nums) {
        
        if(nums.empty()) return 0;
        
        for(int i = 2; i < nums.size(); i++){
            int maxnum = 0;
            for(int j = 0; j < i-1; j++)
                maxnum = max(nums[j], maxnum);
            nums[i] += maxnum;
            
        }
        return *max_element(nums.begin(), nums.end());
        
    }
};