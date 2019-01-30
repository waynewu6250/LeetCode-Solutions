//
// Created by 吳亭緯 on 2018-12-27.
//

#include <iostream>
#include <iomanip>

using namespace std;
void showdata(int *, int);
void selection(int *, int);

int main(){
    int size = 5;
    int d[5] = {4,52,23,2,1};
    cout << "Selection Sort\nOriginal Data:\t";
    showdata(d, size);
    selection(d, size);
    return 0;

}
void showdata(int d[], int size){

    for(int i=0;i<size;++i){
        cout << setw(2) << d[i] << " ";
    }
    cout << endl;
}

void selection(int d[], int size){
    int num=0;
    for(int i=0; i<=size; i++){

        for(int j=i+1;j<=size;j++) {
            //put the smallest at the front
            if (d[i] > d[j]) {
                int tmp;
                tmp = d[j];
                d[j] = d[i];
                d[i] = tmp;

            }
            num++;

            cout << "Number" << num << ":\t";
            for (int j = 0; j < size; j++) cout << setw(2) << d[j] << " ";
            cout << endl;
        }
    }
    cout << "The result:\t";
    showdata(d, size);
}

