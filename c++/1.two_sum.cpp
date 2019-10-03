#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        map<int, int> dic;
        int number = 0;
        for(vector<int>::iterator it=nums.begin(); it!=nums.end(); it++){
            dic[*it] = number;
            number++;
        }
        
        vector<int> answer(2);
        for(int i=0;i<nums.size();i++){
            if(dic.find(target-nums[i]) != dic.end() && dic[target-nums[i]] != i){
                answer[0] = i;
                answer[1] = dic[target-nums[i]];
                return answer;
            }
        }
        return answer;
    
    }
};
