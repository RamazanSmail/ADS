#include "iostream"
#include <stack>
#include <vector>
#include <map>




using namespace std;

bool is_balanced(string word){
    stack <char> st;
    for (auto i:word){
        if(st.empty()){
            st.push(i);
        }else if(st.top() != i){
            st.push(i);
        }else if(st.top() == i){
            st.pop();
        }
        }

        return st.empty();

    } 


int main(){
    string word; cin >> word;
    
    cout << (is_balanced(word) ? "Yes" : "No");
    return 0;
}