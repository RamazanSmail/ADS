#include <iostream>
using namespace std;

class Node{
public:
    int value;
    Node* Next;
    
};

Node* ReversedList(Node* head){
    Node* prev = NULL;  //prev points to NULL
    Node* curr = head;  //out curr pointer is head
    

    while(curr!= NULL){
        Node* temp = curr->Next; //temp variable that stores the next Node, And it needs to store the link
        curr->Next = prev; //Reversing the list
        prev = curr;  //prev will be pointing to the node
        curr = temp; //Moving to the next node
        
    }
    return prev;

}

void printList(Node* head){
    
    while(head != NULL){
        cout << head->value << " ";
        head = head->Next;
    }
    cout << endl;
}


int main(){
    Node* head = new Node();
    Node* second = new Node();
    Node* third = new Node();

    head->value = 1;
    head->Next = second;
    second->value = 2;
    second->Next = third;
    third->value = 3;
    third->Next = NULL;

    cout << "Original list: " << endl;
    printList(head);
    
    head = ReversedList(head); //Reversed linked list
    cout << "Reversed list: " << endl;
    printList(head);


    return 0;
}