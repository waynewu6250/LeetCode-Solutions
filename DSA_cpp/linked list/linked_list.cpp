//
// Created by 吳亭緯 on 2019-01-07.
//

#include <iostream>
using namespace std;

class LinkedList;    // 為了將class LinkedList設成class ListNode的friend,
// 需要先宣告
class Node{
private:
    int data;
    Node *next;
public:
    Node():data(0),next(0){};
    Node(int a):data(a),next(0){};

    friend class LinkedList;
};

class LinkedList{
private:
    // int size;                // size是用來記錄Linked list的長度, 非必要
    Node* first;            // list的第一個node
public:
    LinkedList():first(0){};
    void PrintList();           // 印出list的所有資料
    void Push_front(int x);     // 在list的開頭新增node
    void Push_back(int x);      // 在list的尾巴新增node
    void Delete(int x);         // 刪除list中的 int x
    void Clear();               // 把整串list刪除
    void Reverse();             // 將list反轉: 7->3->14 => 14->3->7
};

void LinkedList::PrintList(){

    if(first==0){
        cout << "List is empty!!" << endl;
        return;
    }
    Node* ptr=first;
    cout << "Data:";
    while(ptr!=0){
        cout << ptr->data << " ";
        ptr = ptr->next;
    }
    cout << endl;


}

void LinkedList::Push_front(int x){

    Node* newnode = new Node(x);
    newnode->next = first;
    first = newnode;

}

void LinkedList::Push_back(int x){

    Node* newnode = new Node(x);

    //If no node
    if(first==0){
        first = newnode;
        return;
    }

    //
    Node* ptr=first;
    while(ptr->next!=0){
        ptr = ptr->next;
    }
    ptr->next = newnode;

}

void LinkedList::Delete(int x){

    /*主要兩種狀況, 有找到x(在頭, 在中間)
     *            沒有找到x         */

    Node* ptr = first;
    Node* prev = 0;

    while(ptr!=0 && ptr->data!=x){
        prev = ptr;
        ptr = ptr->next;
    }

    //No value
    if(ptr==0){
        cout << "There is no element " << x << endl;
    }
    else if(ptr==first){
        first = first->next;
        delete ptr;
        ptr = 0;
    }
    else{
        prev->next = ptr->next;
        delete ptr;
        ptr = 0;
    }

}

void LinkedList::Clear(){

    while(first!=0){

        Node* ptr = first;
        first = first->next;
        delete ptr;
        ptr = 0;

    }

}

void LinkedList::Reverse(){

    Node* ptr=first;
    Node* prev=0;
    Node* nxt=ptr->next;

    if(first==0 || first->next == 0){
        cout << "List is empty!!" << endl;
        return;
    }

    while(nxt!=0){
        ptr->next = prev;
        prev = ptr;
        ptr = nxt;
        nxt = nxt->next;
    }

    ptr->next = prev;
    first = ptr;
}

int main() {

    LinkedList list;     // 建立LinkedList的object
    list.PrintList();    // 目前list是空的
    list.Delete(4);      // list是空的, 沒有4
    list.Push_back(5);   // list: 5
    list.Push_back(3);   // list: 5 3
    list.Push_front(9);  // list: 9 5 3
    list.PrintList();    // 印出:  9 5 3
    list.Push_back(4);   // list: 9 5 3 4
    list.Delete(9);      // list: 5 3 4
    list.PrintList();    // 印出:  5 3 4
    list.Push_front(8);  // list: 8 5 3 4
    list.PrintList();    // 印出:  8 5 3 4
    list.Reverse();      // list: 4 3 5 8
    list.PrintList();    // 印出:  4 3 5 8
    list.Clear();        // 清空list
    list.PrintList();    // 印出: List is empty.

    return 0;
}



