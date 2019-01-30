//
// Created by 吳亭緯 on 2018-12-27.
//

#include <iostream>
#include <iomanip>

using namespace std;
void showdata(int *, int);
void bubble(int *, int);

int main(){
    int size = 5;
    int d[5] = {4,52,23,2,1};
    cout << "Bubble Sort\nOriginal Data:\t";
    showdata(d, size);
    bubble(d, size);
    return 0;

}
void showdata(int d[], int size){

    for(int i=0;i<size;++i){
        cout << setw(2) << d[i] << " ";
    }
    cout << endl;
}

void bubble(int d[], int size){
    for(int i=size; i>=0; i--){

        int flag=0;
        for(int j=0;j<i;j++){
            if(d[j+1]<d[j]){
                int tmp;
                tmp = d[j];
                d[j] = d[j+1];
                d[j+1] = tmp;
                flag++;
            }

        }
        if (flag==0) break;

        cout<<"Number"<<size-i<<":\t";
        for (int j=0;j<size;j++) cout << setw(2) << d[j] << " ";
        cout<<endl;
    }
    cout << "The result:\t";
    showdata(d, size);
}