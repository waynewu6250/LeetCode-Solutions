//
// Created by 吳亭緯 on 2019-01-08.
//

//1 <- 2 <- 3 <- 4 <- top
#include <iostream>
#include <cstdlib>
#include <iomanip>
using namespace std;

class Node{

public:
    int data;
    Node* next=0;

};

Node* front = 0;
Node* rear = 0;

int isEmpty(){
    if(rear==0) return true;
    else return false;
}

void enqueue(int data){
    Node* newnode = new Node;
    newnode->data = data;
    if(rear==0){
        front = newnode;
    }else{
        rear->next = newnode;
    }
    rear = newnode;

}

int dequeue(){
    Node* ptr;
    int tmp;
    if(isEmpty()){
        cout << "No element in queue!!" << endl;
        return -1;
    }
    else{
        ptr=front;
        tmp = front->data;
        front=front->next;
        delete ptr;
        ptr = 0;
        return tmp;
    }
}

void print(){
    Node* ptr=front;
    while(ptr!=0){
        cout << ptr->data << " ";
        ptr = ptr->next;
    }
    cout << endl;
}

int main(){
    int value;
    cout << "Please enter 10 data:" << endl;
    for(int i=0;i<10;i++){
        cin >> value;
        enqueue(value);
        print();
    }
    cout << "=======================" << endl;
    while(!isEmpty()){
        cout << "Element popped:" << setw(2) << dequeue() << endl;
    }
    return 0;
}
