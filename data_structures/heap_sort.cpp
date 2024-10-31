#include <iostream>
using namespace std;
//NOTION!! This is not fullt properly written sort method, it was written for understanding this sort method
void heapify_down(int i = 0){
    
    int largest = i;
    int n;
    int a[n];
    int left = 2*i + 1;
    int right = 2*i + 2;
    if(left < n && a[left] > a[largest]){
        largest = left;
    }
    if(right < n && a[right] > a[largest]){
        largest = right;
    }
    if(largest != i){
        swap(a[largest], a[i]);
        heapify_down();
    }
}

void buildHeap( int a[], int N){
    int I = (N / 2) - 1;
    for(int i = I; i >= 0; i--){   //bulding it from top to the lower with heapify down
        heapify_down();
    }
}

void pop(int a[], int n){
    swap(a[0], a[n]); //it will delete from the maximum 
    n--;
    heapify_down(0);
}

void heap_sort(){
    int n;
    int a[n];
    buildHeap(a, n);
        for(int i = 0; i < n; i++){
            pop(a, n);  //when it happens n times it will be sorted from higher to lower
        }
    }
