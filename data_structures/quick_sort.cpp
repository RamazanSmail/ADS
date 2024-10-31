#include <iostream>
using namespace std;
/* Steps:
1. Random pivot
2. Swap with the end
3. Do partitioning
4. put pivot between parts
*/

int partition(int *a, int l, int r){
    int p = rand() % (r - l + 1) + l; //picking a pivot as a random number    
    swap(a[p], a[r]);  //putting the pivot to the end
    int pivot = a[r]; 
    int i = l - 1;
    for(int j = l; j <= r - 1; j++){  //loop for right side
        if(a[j] <= pivot){
            i++;
            swap(a[i], a[j]);
        }
    }
    swap(a[i + 1], a[r]);
    return i + 1;
}

void qsort(int *a, int l, int r){
    if(l >= r) return;

    int piv = partition(a, l, r);
    qsort(a, l, piv - 1);   //left side  from a pointer to pivot
    qsort(a, piv + 1, r);   //right side a + piv + 1 to n - piv - 1
    
   
}


int main(){
    int n = 9;
    int a[n] = {4, 8, 2, 1, 9, 0, 7, 6, 5};
    //here a is a pointer to a[0]
    qsort(a, 0, n - 1);
    for(int i = 0; i < n; i++){   
        cout << a[i] << " ";
    }
    cout << endl;
    
    //Time complexity O(nlogn)


    return 0;
}