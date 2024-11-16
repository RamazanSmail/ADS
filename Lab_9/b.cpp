#include <iostream>
#include <string>
using namespace std;

int main() {
    string s, T;
    int K;
    
    
    cin >> s >> K;
    
    
    cin >> T;
    
    int count = 0;
    size_t pos = 0;
    
    
    while ((pos = T.find(s, pos)) != string::npos) {
        count++;
        pos += s.size(); 
    }
    
    
    if (count >= K) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
    
    return 0;
}
