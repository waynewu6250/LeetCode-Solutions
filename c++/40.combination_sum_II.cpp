class Solution {
public:
    
    void recur(vector<vector<int>>& answer, vector<int>& items, vector<int>& candidates, int start, int target){
        
        if(target == 0){
            answer.push_back(items);
            return;
        }
        if(target < 0) return;
        
        for(int i = start; i < candidates.size(); i++){
            if(i > start and candidates[i] == candidates[i-1]) continue;
            items.push_back(candidates[i]);
            recur(answer, items, candidates, i+1, target - candidates[i]);
            items.pop_back();
        }
        
    
    }
    
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        
        sort(candidates.begin(), candidates.end());
        
        vector<vector<int>> answer;
        vector<int> items;
        
        recur(answer, items, candidates, 0, target);
        return answer;
        
        
    }
};