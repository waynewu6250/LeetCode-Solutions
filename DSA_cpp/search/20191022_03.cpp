/*
   @Problem 3:（40 分）
   此題與第二題大致相同，但有以下兩項不同：
   
   1. 兩數列結合時，相同的整數只保留一個。舉例來說，若數列一為3、4、4、9，數列二為5、8、9、12，合併後的數列為3、4、5、8、9、12。
   2. 此題將包含非常多的整數，因此為了要在時間限制內完成，程式的效率將變得有些重要。
      使用第二題那個反覆呼叫函數的作法，可能會讓你在某些測試資料中無法在時限內完成。
*/

/*
   @Input：
   輸入輸出格式與第二題完全相同，且已知 1 ≤ n1 ≤ 1000000、1 ≤ n2 ≤ 1000000、0 ≤ xi ≤ 1000000、0 ≤ yi ≤ 1000000。
*/

/*
   @Output：
   讀入這些資訊後，請依上述規則，輸出將v插入後的數列，任兩個整數間以逗號隔開。
*/

/*
   @Sample Input：
   #sample 1:
    9  1  3  5  6  9 10 23 34 56
    8  1  2  3  4  5  6  7  8
   #sample 2:
    3  1  2  3
    2  1  2
   
   @Sample Output：
   #sample 1: 1,2,3,4,5,6,7,8,9,10,23,34,56
   #sample 2: 1,2,3
*/


#include<iostream>
#include<vector>
using namespace std;

int main()
{
    int input = 0;
    // x:
    int xnums = 0; // total x input numbers
    cin >> xnums;
    vector<int> xarray; // create x array
    // input the x numbers in x array
    for (int i = 0; i < xnums; i++)
    {
        cin >> input;
        xarray.push_back(input);
    }

    // y:
    int ynums = 0; // total y input numbers
    cin >> ynums;
    vector<int> yarray; // create y array
    // input the y numbers in y array
    for (int i = 0; i < ynums; i++)
    {
        cin >> input;
        yarray.push_back(input);
    }

    vector<int> answer;
    int ptr1 = 0;
    int ptr2 = 0;

    while(ptr1 != xarray.size() && ptr2 != yarray.size()){

        if(xarray[ptr1] < yarray[ptr2]){
            if(answer.empty() || xarray[ptr1] != answer[answer.size()-1])
                answer.push_back(xarray[ptr1]);
            ptr1++;
        }else if(xarray[ptr1] > yarray[ptr2]){
            if(answer.empty() || yarray[ptr2] != answer[answer.size()-1])
                answer.push_back(yarray[ptr2]);
            ptr2++;
        }else{
            if(answer.empty() || xarray[ptr1] != answer[answer.size()-1])
                answer.push_back(xarray[ptr1]);
            ptr1++;
            ptr2++;
        }

    }

    if(ptr1 == xarray.size()){
        for(int i = ptr2; i<yarray.size(); i++)
            if(yarray[i] != answer[answer.size()-1])
                answer.push_back(yarray[i]);
    }else{
        for(int i = ptr1; i<xarray.size(); i++)
            if(xarray[i] != answer[answer.size()-1])
                answer.push_back(xarray[i]);
    }

    for(int i = 0; i < answer.size()-1; i++) cout << answer[i] << ",";
    cout << answer[answer.size()-1] << endl;


//    // x + y:
//    int xcnt = 0; // count x
//    int ycnt = 0; // count y
//    int cnt = 0; // count x + y
//    int scnt = 0; // count same number
//    vector<int> xyarray; // create x + y array
//    xyarray.push_back(0);
//    // x + y rearrangement
//    for(int i = 0; i < xnums + ynums;i++)
//    {
//        if (cnt + scnt >= (xnums + ynums))
//            break;
//        else
//        {
//        //cout << "\n" << i << ": \n";
//        if(xcnt < xnums && ycnt < ynums)
//        {
//            if (xarray[0] < yarray[0])
//            {
//                //cout<< "x[0]: " << xarray[0] <<", y[0]: "<< yarray[0]<<" ";
//                if (xarray[0] != xyarray[cnt])
//                {
//                    xyarray.push_back(xarray[0]);
//                    xarray.erase(xarray.begin());
//                    xcnt += 1;
//                    cnt += 1;
//                    //cout << "\n x < y_x != xy: \n xcnt: " << xcnt << ", ycnt: " << ycnt << ", cnt: " << cnt << ", scnt: " << scnt;
//                }
//                else
//                {
//                    xarray.erase(xarray.begin());
//                    xcnt += 1;
//                    scnt += 1;
//                    //cout << "\n x < y_x == xy: \n xcnt: " << xcnt << ", ycnt: " << ycnt << ", cnt: " << cnt << ", scnt: " << scnt;
//                }
//            }
//            else if (xarray[0] > yarray[0])
//            {
//                //cout<< "x[0]: " << xarray[0] <<", y[0]: "<< yarray[0]<<" ";
//                if (yarray[0] != xyarray[cnt])
//                {
//                    xyarray.push_back(yarray[0]);
//                    yarray.erase(yarray.begin());
//                    ycnt += 1;
//                    cnt += 1;
//                    //cout << "\n x > y_x != xy: \n xcnt: " << xcnt << ", ycnt: " << ycnt << ", cnt: " << cnt << ", scnt: " << scnt;
//                }
//                else
//                {
//                    yarray.erase(yarray.begin());
//                    ycnt += 1;
//                    scnt += 1;
//                    //cout << "\n x > y_x == xy: \n xcnt: " << xcnt << ", ycnt: " << ycnt << ", cnt: " << cnt << ", scnt: " << scnt;
//                }
//            }
//            else if (xarray[0] == yarray[0])
//            {
//                //cout<< "x[0]: " << xarray[0] <<", y[0]: "<< yarray[0]<<" ";
//                yarray.erase(yarray.begin());
//                ycnt += 1;
//                if (xarray[0] != xyarray[cnt])
//                {
//                    xyarray.push_back(xarray[0]);
//                    xarray.erase(xarray.begin());
//                    xcnt += 1;
//                    cnt += 1;
//                    scnt += 1;
//                    //cout << "\n x == y_x != xy: \n xcnt: " << xcnt << ", ycnt: " << ycnt << ", cnt: " << cnt << ", scnt: " << scnt;
//                }
//                else
//                {
//                    xarray.erase(xarray.begin());
//                    xcnt += 1;
//                    scnt += 1;
//                    //cout << "\n x == y_x == xy: \n xcnt: " << xcnt << ", ycnt: " << ycnt << ", cnt: " << cnt << ", scnt: " << scnt;
//                }
//            }
//        }
//
//            else if (ycnt == ynums)
//            {
//                //cout<< "x[0]: " << xarray[0] <<", y[0]: "<< yarray[0]<<" ";
//                if (xarray[0] != xyarray[cnt])
//                {
//                    xyarray.push_back(xarray[0]);
//                    xarray.erase(xarray.begin());
//                    xcnt += 1;
//                    cnt += 1;
//                    //cout << "\n x_x != xy: \n xcnt: " << xcnt << ", ycnt: " << ycnt << ", cnt: " << cnt << ", scnt: " << scnt;
//                }
//                else
//                {
//                    xarray.erase(xarray.begin());
//                    xcnt += 1;
//                    scnt += 1;
//                    //cout << "\n x_x == xy: \n xcnt: " << xcnt << ", ycnt: " << ycnt << ", cnt: " << cnt << ", scnt: " << scnt;
//                }
//            }
//            else if (xcnt == xnums)
//            {
//                //cout<< "x[0]: " << xarray[0] <<", y[0]: "<< yarray[0]<<" ";
//                if (yarray[0] != xyarray[cnt])
//                {
//                    xyarray.push_back(yarray[0]);
//                    yarray.erase(yarray.begin());
//                    xcnt += 1;
//                    cnt += 1;
//                    //cout << "\n y_x != xy: \n xcnt: " << xcnt << ", ycnt: " << ycnt << ", cnt: " << cnt << ", scnt: " << scnt;
//                }
//                else
//                {
//                    yarray.erase(yarray.begin());
//                    xcnt += 1;
//                    scnt += 1;
//                    //cout << "\n y_x == xy: \n xcnt: " << xcnt << ", ycnt: " << ycnt << ", cnt: " << cnt << ", scnt: " << scnt;
//                }
//            }
//        }
//    }
//    // print
//    for (int i = 1; i < xnums + ynums - scnt; i++)
//    {
//        cout << xyarray[i] << ",";
//    }
//    cout << xyarray[xnums + ynums - scnt];
    
    return 0;
}