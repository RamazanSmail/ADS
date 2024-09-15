#include <deque>
#include <iostream>
#include <queue>



using namespace std;

int main(){
    deque <int> deq; queue <string> word;
    char cntl; int num;

    while(cin >> cntl && cntl != '!'){
        if(cntl == '+'){
          cin >> num; deq.push_front(num);
        }else if(cntl == '-'){
          cin >> num; deq.push_back(num);
        }else if(cntl == '*'){
          if(deq.empty()){
               word.push ("error");
          }else{
               word.push(to_string(deq.front() + deq.back()));
               deq.pop_back();
               if(!deq.empty()) deq.pop_front();
          }
        }
    }

    while(!word.empty()){
     cout << word.front() << endl;
     word.pop();
    }
    return 0;
}