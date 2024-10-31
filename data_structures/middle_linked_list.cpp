#include <bits/stdc++.h>

using namespace std;

class Node{
public:
    int value;
    Node* Next;
    
};

int GetSizeofList(Node* n){
    int size = 0;
    while(n != NULL){
        size++;
        n = n->Next;    //getting the size of linked list

    }
    return size;
}

void PrintMiddleOftheList(Node* n){
    int length = GetSizeofList(n);
    int mid_index = length / 2; //getting middle index

    while(mid_index--){
        n = n->Next;
    }
    cout << n->value << endl;


}
int main(){
    Node* head = new Node();
    Node* second = new Node();
    Node* third = new Node();
    Node* fourth = new Node();
    Node* fifth = new Node();
    Node* sixth = new Node();

    head -> value = 10;
    head -> Next = second;
    second -> value = 20;
    second -> Next = third;
    third -> value = 30;
    third -> Next = fourth;
    fourth -> value = 40;
    fourth -> Next = fifth;
    fifth -> value = 50;
    fifth -> Next = sixth;
    sixth -> value = 60;
    sixth -> Next = NULL;

    PrintMiddleOftheList(head);
    



    return 0;
}
