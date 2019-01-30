//
// Created by 吳亭緯 on 2018-12-27.
//

#include <iostream>
using namespace std;

int main() {
    // your code goes here
    int size, length, result, left, right, mid, X;
    scanf("%d%d",&size,&length);

    int a[size];
    for(int i=0;i<size;i++)
        scanf("%d",&a[i]);


    for(int i=0;i<length;i++){
        result = -1;
        left = 0;
        right = size-1;
        scanf("%d",&X);
        while (left <= right) {
            mid = (left+right) / 2;
            if (X < a[mid]) right = mid - 1;
            else if (X > a[mid]) left = mid + 1;
            else if (X == a[mid]) {
                result = mid;
                right = mid - 1;
            }
        }
        printf("%d\n",result);

    }

    return 0;
}