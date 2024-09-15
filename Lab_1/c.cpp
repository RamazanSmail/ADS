#include "iostream"
#include <stack>

using namespace std;

stack<char> word_read(string s){
    stack<char> word;
    for (auto i:s){
        if(i == '#'){
            if(!word.empty()) word.pop();
        }else{
            word.push(i);
        }
    }
    return word;
}

int main(){
    string s1, s2;
    cin >> s1 >> s2;

    stack <char> c1 = word_read(s1);
    stack <char> c2 = word_read(s2);

    if(c1.size() != c2.size()){
        cout << "No";
        return 0;
    }else{
        for (int i = 0; i < c1.size(); i++)
        {
            if(c1.top() != c2.top()){
                cout << "No";
                return 0;
            }
            c1.pop();
            c2.pop();
        }
        
    }

    cout << "Yes";
    return 0;
}