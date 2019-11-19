class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        
        int islands = 0;
        for(int i = 0; i < grid.size(); i++){
            
            for(int j = 0; j < grid[0].size(); j++){
                
                if(grid[i][j] == '1'){
                    grid[i][j] = '0';
                    bfs(grid, i, j);
                    islands += 1;
                }
            }
            
        }
        return islands;  
        
    }
    
    void bfs(vector<vector<char>>& grid, int i, int j){
        
        pair<int, int> point(i, j);
        queue<pair<int, int>> q;
        q.push(point);
        
        while(!q.empty()){
            
            pair<int, int> axis = q.front();
            q.pop();
                
            int x_inc[4] = {0, 0, 1, -1};
            int y_inc[4] = {1, -1, 0, 0};
            for(int i=0; i<4; i++){
                int x = axis.first + x_inc[i];
                int y = axis.second + y_inc[i];
                if(((x >= 0 && x < grid.size()) && (y >= 0 && y < grid[0].size())) && grid[x][y] == '1'){
                    pair<int, int> new_point(x, y);
                    q.push(new_point);
                    grid[x][y] = '0';
                }
            }
            
        }
        
        
        
    }
};