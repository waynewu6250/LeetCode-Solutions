/*
   @Problem 1:（20 分）
   此題將給定一個無向圖，請判斷其中的n個邊是否能構成迴路（cycle）。以下圖為例：
   
   (1)-----(3)     (6)
    | \     | \   / |
    |  \    |  \ /  |
    |   \   |  (5)  | 
    |    \  |  / \  |
    |     \ | /   \ |
   (2)-----(4)     (7)

   我們可以使用一個鄰接矩陣（adjacency matrix）

   -               -
   | 0 1 1 1 0 0 0 |
   | 1 0 0 1 0 0 0 |
   | 1 0 0 1 1 0 0 |
   | 1 1 1 0 1 0 0 |
   | 0 0 1 1 0 1 1 |
   | 0 0 0 0 1 0 1 |
   | 0 0 0 0 1 1 0 |
   -               -     

   來表示此一無向圖。針對給定的一組邊，首先請檢查這些邊是否都存在於給定的圖中。如果有，則進一步判斷是否包含迴路。
   請依以下規則輸出結果：

   1.若給定的n個邊包含任一條不存在的邊，例如[1, 6]，請輸出0。
   2.若給定的n個邊都存在且不包含環形，例如[1, 3]、[3, 4]、[4, 5]，請輸出2。
   3.若給定的n個邊都存在且包含環形，例如[1, 3]、[3, 5]、[4, 5]、[1, 4]，請輸出1。 
*/

/*
   @Input：
   系統會提供一共10組測試資料，每組測試資料裝在一個檔案裡。
   每個檔案中會有m + k + 2列，第一列含有2個正整數，第一個正整數為n，表示此無向圖中共有n個點，第二個正整數為m，表示此無向圖共有多少條邊。
   第二列到第m + 1列皆含有2個正整數，分別為一個邊的兩個端點的編號，第二列存有i1、j1，第三列存有i2、j2，
   依此類推直到im、jm，每列都是編號小的點列在前面且這m列中不同列的資料不重複。
   第m + 2列包含一個正整數k，表示將選取幾條邊來判斷是否有迴圈，第m + 3列到第m + k + 2列皆含有兩個正整數，第m + 3列為u1、v1，
   第m + 4列為u2、v2，依此類推直到um、vm，每列都是編號小的點列在前面且這k列中不同列的資料不重複。
   已知2 ≤ n ≤ 100、1 ≤ m ≤ 500、1 ≤ k ≤ 500，且點的編號皆為介於1和n（包含1和n）的正整數。
*/

/*
   @Output：
   讀入這些資訊後，請依上述規則輸出一個數字。
*/

/*
   @Sample Input：
   #sample 1:
    7 10
    1  2
    1  3
    1  4
    2  4
    3  4
    3  5
    4  5
    5  6
    5  7
    6  7
    3
    1  3
    3  4
    4  5
   #sample 2:
    7 10
    1  2
    1  3
    1  4
    2  4
    3  4
    3  5
    4  5
    5  6
    5  7
    6  7
    4
    1  3
    3  5
    4  5
    1  4
   #sample 3:
    7 10
    1  2
    1  3
    1  4
    2  4
    3  4
    3  5
    4  5
    5  6
    5  7
    6  7
    3
    1  3
    3  6
    6  7

   @Sample Output：
   #sample 1: 2
   #sample 2: 1
   #sample 3: 0
*/

#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;

int main()
{
    // create n x n array: -----------------------------------

    int n = 0; // nodes
    int m = 0; // lines
    cin >> n >> m;

    vector<vector<int> > adjacent(n+1, vector<int> (n+1, 0));
    int node1 = 0; // node i
    int node2 = 0; // node j
    for(int i=0;i<m;i++)
    {
        cin >> node1 >> node2;
        adjacent[node1][node2] = 1;
        adjacent[node2][node1] = 1;
    }

    // check edges --------------------------------------------
    vector<bool> visited(n);
    int flag = 1;

    // edge
    int edges = 0;
    cin >> edges;
    for(int i=0;i<edges;i++){
        cin >> node1 >> node2;
        if(adjacent[node1][node2] == 0){
            cout << 0;
            flag = 0;
            break;
        }else{
            if(visited[node1] and visited[node2]){
                cout << 1;
                flag = 0;
                break;
            }
            else{
                visited[node1] = true;
			    visited[node2] = true;
            }
            
        }
    }

    if(flag) cout << 2;


    return 0;
}







//    // check loop: -------------------------------------------
//
//    int k = 0; // check loop
//    cin >> k;
//
//    vector<int> check;
//    int uk = 0;
//    int keep = 0;
//    int u = 0; // node u
//    int v = 0; // node v
//    int chcnt = 2; // run k - 1 times (no 1st)
//    int cnt = 0; // check count
//    int change = 0;
//
//    cin >> uk >> keep;
//    if (adjacent[uk][keep] != 1)
//        cout << 0;
//
//    while (chcnt <= k)
//    {
//        cin >> u >> v;
//
//        if (u > v)
//        {
//            change = u;
//            u = v;
//            v = change;
//        }
//
//        if (adjacent[u][v] != 1)
//        {
//            cout << 0;
//            break;
//        }
//        else
//        {
//            if (keep == u)
//                keep = v;
//            else if (keep == v)
//                keep = u;
//
//            if (chcnt == k)
//            {
//                if (keep == uk)
//                    cout << 1;
//                else
//                    cout << 2;
//            }
//            chcnt++;
//        }
//    }
//    return 0;
//}