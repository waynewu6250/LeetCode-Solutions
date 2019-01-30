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

class point{
public:
    node* first;
    node* last;
    point():first(0),last(0){};
};

point list[9]; //put the points inside
int has_run[9]={0}; //see if the point has been searched

//Make a queue to put point inside
int queue[10];
int front=-1; //queue's first
int rear=-1; //queue's last

void enqueue(int value){
    if(rear>=10) return;
    queue[rear++] = value;
}
int dequeue(){
    if(front==rear) return -1;
    return queue[front++];
}

/*///////////////////////////////////////////////////////*/

void print(point* list){

    for(int i=0;i<9;i++){

        node* ptr=list[i].first;

        cout << "Point " << i << "=>";

        while(ptr!=0){
            cout << ptr->value << " ";
            ptr = ptr-> next;
        }
        cout << endl;
    }
}



void bfs(int current, point* list){

    node* ptr;
    enqueue(current); //put inside queue

    has_run[current]=1;
    cout << current << " ";

    while(front!=rear){

        //take out the first element in queue
        current=dequeue();
        ptr=list[current].first;

        // put all the linked nodes inside queue
        while(ptr!=0){
            if(has_run[ptr->value]==0){
                enqueue(ptr->value);
                has_run[ptr->value]=1;
                cout << ptr->value << " ";
            }
            ptr = ptr->next;
        }
    }

}

int main(){

    int data[20][2] = {{1,2},{2,1},{1,3},{3,1},
                       {2,4},{4,2},{2,5},{5,2},
                       {3,6},{6,3},{3,7},{7,3},
                       {4,5},{5,4},{6,7},{7,6},
                       {5,8},{8,5},{6,8},{8,6}};

    for(int i=0;i<9;i++){

        list[i] = point();

        for(int j=0;j<20;j++){
            // according to vertex
            if(data[j][0]==i){

                node* newnode = new node(data[j][1]);
                if(list[i].first==0){
                    list[i].first=newnode;
                    list[i].last=newnode;
                }else{
                    list[i].last->next = newnode;
                    list[i].last = newnode;
                }

            }

        }

    }

    cout << "The graph with linked list method is shown: " << endl;
    print(list);
    cout << endl;

    cout << "BFS print:" << endl;
    bfs(1,list);

}
