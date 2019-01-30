//
// Created by 吳亭緯 on 2018-12-18.
//

#include <iostream>
#include <string>

using namespace std;

class Stack{

public:

    int stack[100], ind;


    Stack(){};
    void push(char x){
        ++ind;
        stack[ind] = x;
    }

    void pop(){
        stack[ind] = 0;
        --ind;
    }

    int top(){
        return stack[ind];
    }

    bool isEmpty() {
        if (ind >= 1)
            return false;
        else return true;
    }
};


bool verify() {

    Stack container = Stack();

    string s = "()[](";
    for(int i=0;i<s.length();i++){
        if(s[i] == '(' or s[i] == '[' or s[i] == '{'){
            container.push(s[i]);
        }
        if (s[i] == ')') {
            if (container.isEmpty() || container.top() != '(') return false;
            else container.pop();
        }
        if (s[i] == ']') {
            if (container.isEmpty() || container.top() != '[') return false;
            else container.pop();
        }
        if (s[i] == '}') {
            if (container.isEmpty() || container.top() != '{') return false;
            else container.pop();
        }
    }
    if(container.ind == 0) return true;
    else return false;

}

int main(){
    cout << verify();
}

