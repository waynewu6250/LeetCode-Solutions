#include <iostream>
using namespace std;

int stack[100], ind;

void push(int x){
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

bool isEmpty(){
    if (ind >= 1)
        return false;
    else return true;
}

int main() {

    ind = 0;
    push(1);
    push(2);
    pop();
    cout << top();

    return 0;
}