//
// Created by 吳亭緯 on 2019-01-09.
//
#include <iostream>
using namespace std;


class TreeNode{
public:

    int data;
    TreeNode *left;
    TreeNode *right;

    TreeNode():data(0),left(0),right(0){};
    TreeNode(int a):data(a),left(0), right(0){};
};

TreeNode* rootnode=0;

void push(int value){
    TreeNode* newnode = new TreeNode(value);
    TreeNode* ptr=0;
    int flag=0;

    if(rootnode==0){
        rootnode = newnode;
    }else{

        ptr = rootnode;
        while(!flag){
            //right tree
            if(newnode->data > ptr->data){
                if(ptr->right==0) {
                    ptr->right = newnode;
                    flag = 1;
                }else ptr = ptr->right;
            }
            //left tree
            else{
                if(ptr->left==0) {
                    ptr->left = newnode;
                    flag = 1;
                }else ptr = ptr->left;
            }

        }
    }
}

void inorder(TreeNode * ptr){

    if(ptr != 0){

        inorder(ptr->left);
        cout << ptr->data << " ";
        inorder(ptr->right);

    }
}
void preorder(TreeNode * ptr){

    if(ptr != 0){

        cout << ptr->data << " ";
        preorder(ptr->left);
        preorder(ptr->right);

    }
}
void postorder(TreeNode * ptr){

    if(ptr != 0){

        postorder(ptr->left);
        postorder(ptr->right);
        cout << ptr->data << " ";

    }
}

TreeNode* search(TreeNode * ptr, int value){
    int i = 1;
    while(1){
        if(ptr==0) return 0;
        else if(ptr->data==value){
            cout << "Times of search: " << i << endl;
            return ptr;
        }
        else{
            if(value<ptr->data) ptr = ptr->left;
            else ptr = ptr->right;
        }
        i++;

    }


}

int main(){

    int value;
    cout << "Please input 10 data: " << endl;
    for(int i=0;i<10;i++){
        cin>>value;
        push(value);
    }
    cout << "Input is done!!" << endl;

    //Print
    cout << "Inorder print:" << endl;
    inorder(rootnode);
    cout << endl;
    cout << "Preorder print:" << endl;
    preorder(rootnode);
    cout << endl;
    cout << "Postorder print:" << endl;
    postorder(rootnode);
    cout << endl;

    //Search
    int svalue;
    cout << "Please insert the value you would like to find:" << endl;
    cin >> svalue;
    if(search(rootnode,svalue) != 0){
        cout << "We have found the value!!" << endl;
    }else{
        cout << "We don't have found the value!!" << endl;
    }



};
