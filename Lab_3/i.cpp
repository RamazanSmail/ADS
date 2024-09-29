#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> v(n);
    for(int i = 0; i < n; i++){
        int element;
        cin >> element;
        v.push_back(element);
    }
    
    int x;
    cin >> x;
    bool f = false;

    int left = 0;
    int right = v.size() - 1;
    int cnt = 0;


    while (left <= right){
        int mid = (left + right) / 2;
        if(v[mid] == x){
            f = true;
            break;
        }
        else if(x > v[mid]){
            left = mid + 1;
        }
        else if(x < v[mid]){
            right = mid - 1;
        }
        else if(ceil(log2(n)) > cnt){
            f = false;
            break;
        }
        

        cnt++;
    }

    if(f) cout << "Yes";
    else cout << "No";
 
    




}