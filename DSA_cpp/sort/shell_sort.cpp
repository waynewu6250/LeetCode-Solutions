//
// Created by 吳亭緯 on 2018-12-28.
//

#include <iostream>
#include <iomanip>

using namespace std;
void showdata(int *, int);
void shell(int *, int);

int main(){
    int size = 5;
    int d[5] = {4,52,23,2,1};
    cout << "Shell Sort\nOriginal Data:\t";
    showdata(d, size);
    shell(d, size);
    return 0;

}
void showdata(int d[], int size){

    for(int i=0;i<size;++i){
        cout << setw(2) << d[i] << " ";
    }
    cout << endl;
}

void shell(int d[], int size){
    int num=1;
    int jmp=size/2;
    int tmp;

    while(jmp!=0){

        for (int i=jmp;i<size;i++){
            tmp = d[i]; //the second element
            int j=i-jmp; //the first element
            while(tmp<d[j] && j>=0){
                d[j+jmp] = d[j];
                j=j-jmp;
            }
            d[jmp+j]=tmp;

        }
        cout << "Number" << num++ << ":\t";
        showdata(d,size);
        jmp /= 2;


    }
    cout << "The result:\t";
    showdata(d, size);
}