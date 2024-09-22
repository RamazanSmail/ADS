#include<iostream>
#include<vector>

using namespace std;

int main(){
    int n;
    int k;
    vector<string> poem;
    cin >> n >> k;
    for(int i = 0; i < n; i++){
        string s;
        cin >> s;
        poem.push_back(s);
    }
    for(int i = k; i < poem.size(); i++){
        cout << poem[i] << " ";
    }
    for(int i = 0; i < k; i++){
        cout << poem[i] << " ";
    }


    return 0;
}