//
// Created by 吳亭緯 on 2018-12-28.
//
#include <iostream>
#include <iomanip>

using namespace std;
void showdata(int *, int);
void insertion(int *, int);

int main(){
    int size = 5;
    int d[5] = {4,52,23,2,1};
    cout << "Insertion Sort\nOriginal Data:\t";
    showdata(d, size);
    insertion(d, size);
    return 0;

}
void showdata(int d[], int size){

    for(int i=0;i<size;++i){
        cout << setw(2) << d[i] << " ";
    }
    cout << endl;
}

void insertion(int d[], int size){
    int num=0;
    for(int i=1; i<=size; i++){

        for(int j=0;j<i;j++) {
            //put the element inside sorted elements
            if (d[i] < d[j]) {
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
