//
// Created by 吳亭緯 on 2019-01-03.
//

#include <iostream>
#include <iomanip>
#include <ctime>
#include <cstdlib>


using namespace std;
void showdata(int *, int);
void quick(int *, int, int, int);
int num=0;

int main(){
    int size = 5;
    int d[5] = {4,52,23,2,1};
    cout << "Quick Sort\nOriginal Data:\t";
    showdata(d, size);
    quick(d, size, 0, size-1);
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

void quick(int d[], int size, int lf, int rg){
    int tmp;
    int lf_idx;
    int rg_idx;

    if (lf<rg){

        lf_idx = lf+1;
        rg_idx = rg;

        //Operation 1
        while(1){

            cout << "Number" << num++ << ":\t";
            showdata(d, size);

            //Find larger number at the left
            for(int i=lf+1;i<=rg;i++){
                if(d[i]>=d[lf]){
                    lf_idx = i;
                    break;
                }
                lf_idx++;
            }
            //Find smaller number at the right
            for(int i=rg;i>=lf+1;i--){
                if(d[i]<=d[lf]){
                    rg_idx = i;
                    break;
                }
                rg_idx--;
            }
            //Switch two numbers
            if(lf_idx<rg_idx){
                tmp = d[lf_idx];
                d[lf_idx] = d[rg_idx];
                d[rg_idx] = tmp;
            }else break;

        }

        //Operation 2
        if(lf_idx>=rg_idx){
            tmp = d[lf];
            d[lf] = d[rg_idx];
            d[rg_idx] = tmp;

            //Do recursion based on rg_idx as middle
            quick(d,size,lf,rg_idx-1);
            quick(d,size,rg_idx+1,rg);

        }


    }

}