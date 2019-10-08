/*
   @Problem 2:（40 分）
   承上題，但在此題我們將使用不同的演算法。
   演算法將執行min{m, n}輪，每一輪我們都搜尋整張表並尋找仍可配對的權重中最大的值。
   也就是，對所有還未被配對的列和欄，找出i∗_k、j∗_k使得wi∗k,j∗k ≥ wij，若有複數個點相等且皆為最大值，先選擇i最小的，再選擇j最小的。

   以下表為例：
   -----------------
   | 4 | 2 | 0 | 3 |
   |---------------|
   | 5 | 1 | 5 | 2 |
   |---------------|
   | 3 | 2 | 0 | 3 |
   -----------------
   
   第一次搜索後發現權重最大的是w21 = w23 = 5，且兩者的i相同，但w21的j較小，因此選擇i∗_1 = 2、j∗_1 = 1。
   接下來用同樣規則繼續選擇，除了第2列及第1欄以外權重最大且i、j較小的為i∗_2 = 1、j∗_2 = 4，其權重為3。
   最後再選擇i∗_3 = 3、j∗_3 = 2、其權重為2。如此即求得一組解，其總配對權重為10。
*/

/*
   @Input：
   系統會提供一共 20 組測試資料，每組測試資料裝在一個檔案裡。
   輸入格式和第二題一模一樣。
*/

/*
   @Output：
   讀入這些數字之後，請依上述規則，依序輸出每一次的i∗_k及j∗_k，i∗_k及j∗_k中間以逗號隔開，而每一次的輸出則以分號隔開。
   最後一輪的輸出之後輸出一個分號，最後再輸出總配對權重。
*/

/*
   @Sample Input：
   #sample 1
   3 4
   4 2 0 3
   5 1 5 2
   3 0 2 3
   #sample 2
   6 4
   4 2 9 3
   1 4 5 8
   5 7 6 8
   2 3 5 3
   4 9 4 6
   7 5 3 7
   
   @Sample Output：
   #sample 1: 2,1;1,4;3,3;10
   #sample 2: 1,3;5,2;2,4;6,1;33
*/

#include <iostream>
#include <vector>
using namespace std;

int main()
{

    int m=0;
    int n=0;
    cin >> m >> n;

    vector<vector<int>> contents;

    for (int i = 0; i < m; ++i) {
        vector<int> vi;
        for (int j = 0; j < n; ++j){
            int val;
            cin >> val;
            vi.push_back(val);
        }
        contents.push_back(vi);

    }

    /*//////*/

    int row[m];
    int col[n];
    for (int i = 0; i < m; ++i) row[i]=0;
    for (int i = 0; i < n; ++i) col[i]=0;

    int maxrow = 0;
    int maxcol = 0;
    int weights = 0;

    int rounds = min(m, n);

    int i = 0;
    while(i < rounds){
        int max=0;
        for (int i = 0; i < m; ++i) {
            if(row[i] == 1) continue;
            for (int j = 0; j < n; ++j){
                if(col[j] == 1) continue;
                if(contents[i][j] > max){
                    max = contents[i][j];
                    maxrow = i;
                    maxcol = j;
                }
            }
        }
        row[maxrow] = 1;
        col[maxcol] = 1;
        cout << maxrow+1 << "," << maxcol+1 << ";";
        weights += max;
        i++;

    }
    cout << weights;

    
    return 0;
}