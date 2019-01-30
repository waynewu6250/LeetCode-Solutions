//
// Created by 吳亭緯 on 2019-01-14.
//
#include <iostream>
using namespace std;

class edge{

public:
    int from, to, val;
    int find;
    edge* next;

    edge(int f, int t, int v):from(f),to(t),val(v),find(0),next(0){};

};

void print(edge* ptr){
    while(ptr!=0){
        cout << "from: " << ptr->from << " to: " << ptr->to << " value: " << ptr->val << endl;
        ptr=ptr->next;
    }

}

edge* findmincost(edge* root){

    edge* ptr, *getptr;
    ptr = root;
    int minval=100;

    while(ptr!=0){
        if(ptr->val<minval && ptr->find==0){
            minval = ptr->val;
            getptr = ptr;
        }
        ptr = ptr->next;
    }
    getptr->find = 1;
    return getptr;


}

void mintree(edge* root){

    edge* ptr, *getptr;
    ptr = root;

    int result = 0;
    int v[7] = {0};

    while(ptr!=0){


        //find the edge with the smallest value
        getptr = findmincost(root);

        //check if the from and to of this edge has been called
        v[getptr->from]++;
        v[getptr->to]++;

        if(v[getptr->from] > 1 && v[getptr->to] > 1){
            v[getptr->from]--;
            v[getptr->to]--;
            result=1;
        }
        else{
            result=0;
        }
        if(result==0){
            cout << "from: " << getptr->from << " to: " << getptr->to << " value: " << getptr->val << endl;
        }
        ptr = ptr->next;

    }


};




int main(){

    int data[10][3] = {{1,2,6}, {1,6,12},
                       {1,5,10}, {2,3,3},
                       {2,4,5}, {2,6,8},
                       {3,4,7}, {4,6,11},
                       {4,5,9}, {5,6,16}};

    edge* root=0, *ptr, *newnode;
    for(int i=0;i<10;i++){

        for(int j=1;j<=6; j++){

            if(data[i][0]==j){
                newnode = new edge(data[i][0], data[i][1], data[i][2]);
                if(root==0){
                    root=newnode;
                    ptr=root;
                }else{
                    ptr->next = newnode;
                    ptr = ptr->next;
                }
            }
        }

    }

    print(root);

    //Set up mintree
    cout << endl << "Set up mintree" << endl;
    mintree(root);
    delete newnode;


}
