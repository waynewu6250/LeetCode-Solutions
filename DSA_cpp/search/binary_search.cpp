//
// Created by 吳亭緯 on 2018-12-22.
//

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream f("data.in");
ofstream g("data.out");

int A[1000], numberElements;

int BinarySearch(int X){
    int Left=1, Right=numberElements, mid;

    while(Left <= Right){
        mid = (Left+Right) / 2;
        if(X==A[mid]) return mid;
        else if(X<A[mid]) Right=mid-1;
        else Left=mid+1;
    }
    return -1;
}

int main(){

    int answer;
    f>>numberElements;
    for(int i=0; i<numberElements; ++i){
        f>>A[i];
    }
    answer = BinarySearch(5);
    cout << answer;
    g.write(answer);
}