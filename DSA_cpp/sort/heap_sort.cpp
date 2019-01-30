//
// Created by 吳亭緯 on 2019-01-03.
//

#include <iostream>
#include <iomanip>
#include <ctime>
#include <cstdlib>


using namespace std;
void showdata(int *, int);
void heap(int *, int);
void ad_heap(int *, int, int);
int num=0;

int main(){
    int size = 5;
    int d[5] = {4,52,23,2,1};
    cout << "Quick Sort\nOriginal Data:\t";
    showdata(d, size);
    heap(d, size);
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

void heap(int d[], int size){

    int tmp;

    //1. Make heap tree
    for(int i=size/2;i>0;i--){
        ad_heap(d,i,size-1);
    }
    cout << "Number" << num++ << ":\t";
    showdata(d,size);

    //2. Heap sort
    for(int i=size-2;i>0;i--){
        tmp=d[i+1];
        d[i+1]=d[1];
        d[1]=tmp;
        ad_heap(d,1,i);
        cout << "Number" << num++ << ":\t";
        showdata(d, size);
    }

}

void ad_heap(int d[], int i, int size){

    int post=0;
    int j=2*i;
    int tmp=d[i];

    while(j<=size && post==0){

        //find largest element
        if(j<size){
            if(d[j]<d[j+1]) j++;
        }

        if(tmp>=d[j]) post=1; //end
        else{
            d[j/2]=d[j];
            j=2*j;
        }
    }
    d[j/2]=tmp;


}