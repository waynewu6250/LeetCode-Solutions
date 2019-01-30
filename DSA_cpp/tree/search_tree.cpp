//
// Created by 吳亭緯 on 2019-01-09.
//
#include <iostream>
using namespace std;


class Tree{
private:
    int data;
    Tree *left;
    Tree *right;
public:
    Tree():data(0),left(0),right(0){};
    Tree(int a):data(a),right(0){};
};

int main(){
    int level;
    int d[] = {0,6,3,5,9,7,8,4,2};
    int btree[16]={0};

    //Print original data
    cout << "Original data: " << endl;
    for(int i=1;i<9;i++){
        cout << d[i] << " ";
    }
    cout << endl;

    //build up tree
    for(int i=1;i<9;i++){

        for(level = 1;btree[level]!=0;){
            if(d[i]>btree[level])
                level = level*2+1;
            else level = level*2;
        }
        btree[level] = d[i];

    }

    //Print tree
    cout << "Tree data: " << endl;
    for(int i=0;i<16;i++){
        cout << btree[i] << " ";
    }
}
