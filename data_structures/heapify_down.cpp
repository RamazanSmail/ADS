#include <iostream>
using namespace std;

void heapify_down(){ //using for deleting top element 
    int n;
    int a[n];
    int i = 0;
    int largest = i; //largest value in heap is at the 0 index
    int left = 2*i + 1; //index of left child
    int right = 2*i + 2; //index of right child
    if(left < n && a[left] > a[largest]){ 
        a[largest] = a[left]; 
    }
    if(right < n && a[right] > a[largest]){
        a[largest] = a[right];
    }
    if(largest != i){ 
        swap(a[largest], a[i]); //recursive part where it stops when largest will be equal to the index
        heapify_down();   
    }
}

int main(){}
