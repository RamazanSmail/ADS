#include <iostream>
#include <queue>




using namespace std;

int main(){
    int size; string choice;
    queue<int> s, k;
    
    cin >> size >> choice;
    
    for(int i = 0; i < size; i++){
        choice[i] == 'S' ? s.push(i) : k.push(i);
    }
    int s_index, k_index;
    while(!s.empty() and !k.empty()){
        s_index = s.front();
        k_index = k.front();
        
        s.pop();k.pop();
        
        if(s_index < k_index){
            s.push(s_index+size);
        }
        else{
            k.push(k_index+size);
        }
    }
    cout << (s.empty() ? "KATSURAGI" : "SAKAYANAGI");
}