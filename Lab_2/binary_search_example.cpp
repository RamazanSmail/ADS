#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n, item;
    cout << "Print number of elements in array: ";
    cin >> n;
    vector<int> v;
    cout << "Print elements of array: ";
    for(int i = 0; i < n; i++){
        int element;
        cin >> element;
        v.push_back(element);
    }

    cout << "Print number to find: ";
    cin >> item;
    int high = v.size() - 1; 
    int low = 0;
    int cnt = 0;
    
    
    while(low <= high){
       int mid = (low + high) / 2;
       int guess = v[mid];
       if(guess == item){
            cout << "Element is: " << v[mid] << endl;
            break;
       }
       if(guess > item){
        high = mid - 1;
        
       }
       else{
        low = mid + 1;
        
       }
       cnt++;
    }

cout << "Digit is found in: "<< cnt;
  




}