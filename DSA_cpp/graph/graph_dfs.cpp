//
// Created by 吳亭緯 on 2019-01-11.
//
#include <iostream>
using namespace std;

class node{

public:
    int value;
    node* next;

    node():value(0),next(0){};
    node(int v):value(v),next(0){};

};

node* list[9]; //put the points inside
int has_run[9]={0}; //see if the point has been searched

/*///////////////////////////////////////////////////////*/

void print(node** list){
    for(int i=0;i<9;i++){

        node* ptr=list[i];

        cout << "Point " << i << "=>";

        while(ptr!=0){
            cout << ptr->value << " ";
            ptr = ptr-> next;
        }
        cout << endl;
    }
}

void dfs(int current, node** list){

    has_run[current]=1;
    cout << current << " ";

    node *ptr = list[current]->next;
    while(ptr!=0){
        if(has_run[ptr->value]==0)
            dfs(ptr->value, list);
        ptr = ptr->next;
    }

}

int main(){

    node *ptr,*newnode;

    int data[20][2] = {{1,2},{2,1},{1,3},{3,1},
                       {2,4},{4,2},{2,5},{5,2},
                       {3,6},{6,3},{3,7},{7,3},
                       {4,5},{5,4},{6,7},{7,6},
                       {5,8},{8,5},{6,8},{8,6}};
    for(int i=0;i<9;i++){

        list[i] = new node(i);
        ptr=list[i];

        for(int j=0;j<20;j++){
            // according to vertex
            if(data[j][0]==i){

                newnode = new node(data[j][1]);
                do{
                    ptr->next=newnode;
                    ptr=ptr->next;
                }while(ptr->next!=0);

            }

        }

    }

    cout << "The graph with linked list method is shown: " << endl;
    print(list);
    cout << endl;

    cout << "DFS print:" << endl;
    dfs(1,list);


}