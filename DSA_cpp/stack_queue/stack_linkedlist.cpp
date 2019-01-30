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

Node* top = 0;

int isEmpty(){
    if(top==0) return true;
    else return false;
}

void push(int data){
    Node* newnode = new Node;
    newnode->data = data;
    newnode->next = top;
    top = newnode;
}

int pop(){
    Node* ptr;
    int tmp;
    if(isEmpty()){
        cout << "No element in stack!!" << endl;
        return -1;
    }
    else{
        ptr=top;
        top=top->next;
        tmp = ptr->data;
        delete ptr;
        ptr = 0;
        return tmp;
    }
}

int main(){
    int value;
    cout << "Please enter 10 data:" << endl;
    for(int i=0;i<10;i++){
        cin >> value;
        push(value);
    }
    cout << "=======================" << endl;
    while(!isEmpty()){
        cout << "Element popped:" << setw(2) << pop() << endl;
    }
    return 0;
}