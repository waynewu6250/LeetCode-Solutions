class Solution {
public:
     vector<vector<int>> recur(vector<int>& items, vector<vector<int>> answer, int start, int k, int n){
        if(items.size() > k)
            return answer;
         
        if(items.size() == k)
            answer.push_back(items);
        
        for(int i = start; i<=n; i++){
            items.push_back(i);
            answer = recur(items, answer, i+1, k, n);
            items.pop_back();
        }
        return answer;
        
    }
    
    vector<vector<int>> combine(int n, int k) {
        
        vector<vector<int>> answer;
        vector<int> items;
        
        return recur(items, answer, 1, k, n);
        
    }
};