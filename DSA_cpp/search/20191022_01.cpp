/*
   @Problem 1:（20 分）
   給定一個按大小排序過的整數數列x1、x2直到xn，其中x1 ≤ x2 ≤ ⋯ ≤ xn。
   請將整數v依大小關係插入正確的位置中。另外，請為此題寫一個函式，傳入及回傳值可以自行設計。
*/

/*
   @Input：
   系統會提供一共10組測試資料，每組測試資料裝在一個檔案裡。
   每個檔案中會有兩列，第一列含有n + 1個整數，第一個正整數為n，第二到第n + 1個整數分別為x1、x2直到xn。第二列含有一個整數v。
   已知1 ≤ n ≤ 500、0 ≤ xi ≤ 200、0 ≤ v ≤ 1000。
*/

/*
   @Output：
   讀入這些資訊後，請依上述規則，輸出將v插入後的數列，任兩個整數間以逗號隔開。
*/

/*
   @Sample Input：
   #sample 1:
    9  1  3  5  6  9 10 23 34 56
   16
   #sample 2:
    3  1  2  3
    2
   
   @Sample Output：
   #sample 1: 1,3,5,6,9,10,16,23,34,56
   #sample 2: 1,2,2,3
*/

#include <iostream>
#include <vector>
using namespace std;

int main()
{
    //Read inputs
    vector<int> array;

    int input = 0;
    int nums = 0; // total input numbers
    int target = 0;

    cin >> nums;

    for(int i=0; i<nums; i++){
        cin >> input;
        array.push_back(input);
    }
    cin >> target;

    int start = 0;
    int end = array.size()-1;

    while(start <= end){

        int mid = (start+end)/2;

        if(target > array[mid])
            start = mid+1;
        if(target <= array[mid])
            end = mid-1;
    }

    array.insert(array.begin()+start, target);

    for(auto i: array){
        cout << i << ",";
    }
    return 0;

}









// arrangement
//void arrange (int array[], int index)
//{
//    for (int i = 0; i < index; i++)
//    {
//        int j = i;
//        while (j > 0 && array[j - 1] > array[j])
//        {
//            int temp = array[j];
//            array[j] = array[j - 1];
//            array[j - 1] = temp;
//            j--;
//        }
//    }
//}
//
//int main()
//{
//    int array[500] = {0};
//
//    int input = 0;
//    int index = 0; // total input numbers
//    int sum = 0; // calculate repeat numbers
//
//    // input the numbers
//    while(cin >> input)
//    {
//        array[index] = input;
//        index++;
//
//        // Press "Enter" and break the while
//        if (getchar() == '\n') break;
//    }
//
//    // calculate repeat numbers and delete them
//    for (int i = 0; i < index; i++)
//    {
//        for (int j = 0; j < i; j++)
//        {
//            if (array[j] == array[i])
//            {
//                array[i] = 0;
//                sum++;
//            }
//        }
//    }
//
//    // add insert
//    cin >> array[index];
//    index += 1;
//
//    // arrangement
//    arrange(array, index + 1);
//
//    // print
//    for (int i = 1 + sum; i < index - 1 + sum; i++)
//    {
//        cout << array[i] << ",";
//    }
//    cout << array[index - 1 +sum];
//
//    return 0;
//}