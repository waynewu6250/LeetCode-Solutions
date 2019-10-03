#include <vector>
using namespace std;

class Solution {
    
public:
    vector<vector<int>> answers;
    
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        
        vector<int> items;
        recur(items, 0, target, candidates);
        return answers;
        
    }
    
    void recur(vector<int>& items, int start, int target, vector<int>& candidates){
        
        if(target == 0){
            answers.push_back(items);
            return;
        } 
        if(target < 0) return;
        for(int i = start; i < candidates.size(); i++){
            items.push_back(candidates[i]);
            recur(items, i, target-candidates[i], candidates);
            items.pop_back();
        }
        
    }
};