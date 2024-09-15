#include <iostream>
#include <deque>
#include <stack>
#include <queue>
#include <vector>

using namespace std;

int main(){
    stack <int> k;
    // 1,2,3,4,5
    // первым зашел первым вышел
    
    queue<int> q;

    q.push(1);
    q.push(3);
    q.push(5);

    cout << "the start " << q.front() << " tail " << q.back();

    q.pop();

    cout << "the start " << q.front() << " tail " << q.back();
    return 0;
}

