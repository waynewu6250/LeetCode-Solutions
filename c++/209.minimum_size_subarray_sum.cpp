class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        
        int left = 0;
        int sum = 0;
        int minlength = INT_MAX;
        
        for(int i=0; i < nums.size(); i++){
            
            sum += nums[i];
            while(sum >= s){
                minlength = min(minlength, i-left+1);
                sum -= nums[left];
                left += 1;
            }
            
        }
        
        return minlength != INT_MAX ? minlength : 0;
        
        
    }
};