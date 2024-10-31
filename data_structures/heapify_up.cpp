#include <iostream>
#include <vector>
using namespace std;


void heapify_up(){  //using for inserting data, starting with the lowest index, going up
    vector<int> v;
    int index = 0;
    int parent;
    
    parent = (index-1)/2; //parent index
    index = 0;
    while(index != 0 && v[parent]<v[index]){
        swap(v[parent], v[index]); //if children is greater than father swap them
        index = parent; //children became in the father position
        parent = (index-1) / 2;
    }
}

int main(){
    heapify_up();
}