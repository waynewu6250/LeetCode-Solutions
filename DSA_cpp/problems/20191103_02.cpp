/*
   @Problem 2:（20 分）
   在本題中，我們將實作Kruskal's algorithm，給定一個加權無向圖，請找出一個「滿足一個特殊限制」（後面會說明）的最小生成樹（minimum cost spanning tree）。
   加權無向圖範例如下：
   
        4
   (1)-----(3)     (6)
    | \     | \  7/ |
    |  \    | 5\ /  |
   6| 10\  3|  (5)  |2
    |    \  | 4/ \  |
    |   2 \ | /  4\ |
   (2)-----(4)     (7)

   我們可以使用一個鄰接矩陣（adjacency matrix）

   -                      -
   | -1  6  4 10 -1 -1 -1 |
   |  6 -1 -1  2 -1 -1 -1 |
   |  4 -1 -1  3  5 -1 -1 |
   | 10  2  3 -1  4 -1 -1 |
   | -1 -1  5  4 -1  7  4 |
   | -1 -1 -1 -1  7 -1  2 |
   | -1 -1 -1 -1  4  2 -1 |
   -                      -     

   來表示此一加權無向圖。

   在實做Kruskal's algorithm去求得最小生成樹時，有以下兩點請注意：

   1.若有兩條邊[i, j]和[u, v]的權重相同，請先挑i + j和u + v中較小的，若仍相同，請先挑min{i, j}和 min{u, v}中較小的。
     舉例來說，若[1, 5]和[2, 4]的權重相同，由於1 + 5和2 + 4也相同，先選擇min{1, 5}和min{2, 4}中較小的，也就是[1, 5]。
   2.在此最小生成樹上，每一個點的分支度（degree）必須小於等於t，也就是一個點不能和超過t個點連接。
     以原圖為例，點4的分支度為4，因為他與點1、點2、點3、點5相連。
     因此在演算法挑選一個邊的時候，不僅要檢查該邊是否會造成迴路，也要檢查該邊是否會使一個點在最小生成樹上有高於t的分支度，任一項成立就要略過這個邊不挑。
*/

/*
   @Input：
   系統會提供一共10組測試資料，每組測試資料裝在一個檔案裡。
   每個檔案中會有m + 1列，第一列含有3個正整數，第一個正整數為n，表示此圖中共有幾個點，第二個正整數為m，表示此圖共有多少條邊，
   第三個正整數為t，表示最小生成樹中每個點的分支度上限。
   第二到第m + 1列皆各含有三個正整數，第二列存有i1、j1、wi1,j1，第三列存有i2、j2、wi2,j2，依此類推直到im、jm、wim,jm。
   已知2 ≤ n ≤ 500、1 ≤ m ≤ 500、1 ≤ w ≤ 100、2 ≤ t ≤ 10，且點的編號皆為介於1和n（包含1和n）的正整數。
*/

/*
   @Output：
   讀入這些資訊後，請依上述規則計算並輸出，其中第一行請輸出一個數字，表示此最小生成樹的總重。
   第二行請按照選擇的順序依序輸出每一條被選擇的邊，每一條邊的兩個數字請以逗號隔開，不同邊請以分號隔開，
   且針對每一條邊請先輸出編號較小的點再輸出較大的點(顯然地，我們會輸出n − 1條邊)。
*/

/*
   @Sample Input：
   #sample 1:
    7 10  3
    1  2  6
    1  3  4
    1  4 10
    2  4  2
    3  4  3
    3  5  5
    4  5  4
    5  6  7
    5  7  4
    6  7  2
   #sample 2:
    6  8  2
    1  2  4
    1  6  6
    2  3  3
    3  4  4
    3  5  9
    3  6  2
    4  5  3
    5  6  5

   @Sample Output：
   #sample 1: 
   19
   2,4;6,7;3,4;1,3;4,5;5,7

   #sample 2:
   17
   3,6;2,3;4,5;1,2;5,6
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
 
struct edge
{
       int start, end;                                
       int cost;                               
       edge(int x,int y, int c):start(x),end(y),cost(c){}

};


bool cmp(edge a, edge b)
{
       
       if(a.cost != b.cost) return a.cost < b.cost;
       else{
              if(a.start+a.end != b.start+b.end) return a.start+a.end < b.start+b.end;
              else return min(a.start,a.end) < min(b.start,b.end);
       }
       
}

int findFather(vector<int> father, int x)
{
       int a = x;
       while (x != father[x])
              x = father[x];
       while (a != father[a]) {
              int z = a;
              a = father[a];
              father[z] = x;
       }
       return x;
}


int main()
{
       int n = 0; // nodes
       int m = 0; // lines
       int t = 0;
       cin >> n >> m >> t;

       int node1 = 0; // node i
       int node2 = 0; // node j
       int cost = 0;
       vector<edge> E;
       vector<int> father(n); 
       for (int i = 0; i < n; i++)              
              father[i] = i;
       vector<edge> edges;
       vector<int> visited(n, 0);

       for(int i=0; i<m; i++){
              cin >> node1 >> node2 >> cost;
              E.push_back(edge(node1, node2, cost));
       }


       sort(E.begin(), E.end(), cmp);
       int weight = 0;
       for (int i = 0; i < m; i++){
              int ind1 = E[i].start-1;
              int ind2 = E[i].end-1;
              int faU = findFather(father, E[i].start);           
              int faV = findFather(father, E[i].end);           

              if (visited[ind1] >= t || visited[ind2] >= t) continue;
              if (faU != faV) {                              
                     father[faU] = faV;
                     weight += E[i].cost;
                     edges.push_back(E[i]);
                     visited[ind1]++;
                     visited[ind2]++;
              }
       }

       cout << weight << endl;
       for(int i = 0; i < edges.size()-1; i++)
              cout << edges[i].start << "," << edges[i].end << ";";
       cout << edges[edges.size()-1].start << "," << edges[edges.size()-1].end << endl;

       return 0;
}