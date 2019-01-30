//
// Created by 吳亭緯 on 2019-01-03.
//

#include <iostream>
#include <iomanip>
#include <ctime>
#include <cstdlib>


using namespace std;
void showdata(int *, int);
void radix(int *, int);
int num=0;

int main(){
    int size = 5;
    int d[5] = {4,52,23,2,1};
    cout << "Quick Sort\nOriginal Data:\t";
    showdata(d, size);
    radix(d, size);
    cout << "The result:\t";
    showdata(d, size);
    return 0;

}
void showdata(int d[], int size){

    for(int i=0;i<size;++i){
        cout << setw(2) << d[i] << " ";
    }
    cout << endl;
}

void radix(int d[], int size){

    for(int n=1;n<=100;n=n*10){

        cout << "Number" << num++ << ":\t";
        showdata(d, size);

        int tmp[10][100] = {};

        // put data into another array
        for(int i=0;i<size;i++){
            int m=(d[i]/n)%10;
            tmp[m][i] = d[i];
        }

        // put data back into original array
        int k = 0;
        for(int i=0;i<10;i++){
            for(int j=0;j<size;j++){
                if(tmp[i][j]!=0){
                    d[k] = tmp[i][j];
                    k++;
                }
            }
        }


    }

}
