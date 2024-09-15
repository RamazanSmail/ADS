#include <iostream>
#include <deque>
#include <stack>
#include <queue>
#include <vector>

using namespace std;

int main(){
    stack <int> k;
    // 1,2,3,4,5
    // первым зашел последним вышел
    // последним зашел первым вышел
    k.empty(); //return true or false
    k.push(1); // 1 
    k.push(2);
    cout << k.size() << "\n";
    if(k.empty()){
        cout << "Stack is empty";
    }else{
        cout << "stack is not empty";
    }

    cout << endl << k.top();



    cout << endl << k.top();

    
    if(k.empty()){
        cout << "Stack is empty";
    }else{
        cout << "stack is not empty";
    }

    k.emplace(3);
    cout << k.top();
    return 0;
}

