#include <iostream>
#include <cassert>
#include <vector>

using namespace std;

void merge(int *a, int n, int *b, int m){
    int left = 0, right = 0;  //left is the pointer of left side, right is the pointer of right side
    vector<int> c; //where we will be store sorted list
    
    while(left < n || right < m){
        if (left == n){ //if the left side is empty we only move right pointer
            c.push_back(b[right]);
            right++;
        }
        else if (right == m){ //if the right side is empty we only move left pointer
            c.push_back(a[left]);
            left++;
        }
        else if (a[left] < b[right]){ //left < n and right < m
            c.push_back(a[left]);
            left++;
        }
        else{
            c.push_back(b[right]);
            right++;
        }
    }
//     assert(c.size() == n + m);
    for(int i = 0; i < n + m; i++){
        a[i] = c[i];
    }
}

void merge_sort(int *a, int n){
    if(n == 1) return;
    int mid = n / 2;
    merge_sort(a, mid); //sorting left part 
    merge_sort(a + mid, n - mid); //sorting right part
    merge(a, mid, a + mid, n - mid);
}

int main(){

    int n = 9;
    int a[n] = {4, 8, 2, 1, 9, 0, 7, 6, 5};
    //here a is a pointer to a[0]
    merge_sort(a, n);
    for(int i = 0; i < n; i++){   
        cout << a[i] << " ";
    }
    cout << endl;
    return 0;
    //Time complexity O(nlogn)
}