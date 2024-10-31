#include <iostream>
using namespace std;

class Node{
public:
    int value; //integer value of element
    Node* Next; //pointer to the next element     
    // [value|Next] - form of the Node
    Node(int val) : value(val), Next(NULL) {}
};

void printList(Node* n){ //access all the elements and print the values of this elements
    while(n != NULL){
        cout<< n -> value << endl;
        n = n -> Next;
    }

}

Node* TakeUserInput(){
    int val;
    Node* head = NULL;
    Node* tail = NULL;
    while(true){
        
        cin >> val;
        if(val == -1) break;
        Node* newNode = new Node(val);

        if(head == NULL){
            head = newNode; //Setting first as a head

            tail = newNode; //Setting first as a tail
        }
        else{
            tail->Next = newNode; //points to the adress of next Node
            tail = newNode; 
        }
        

    }

    return head;
}

int main(){
    // Node* head = new Node();
    // Node* second = new Node();
    // Node* third = new Node();   //we created 3 pointers to 3 nodes
    
    // //Giving values and linking them
    // head -> value = 1; //our first node will store value = 1. -> is used to access membors of class
    // head -> Next = second; //head element will be point to the second element
    // second -> value = 2;
    // second -> Next = third;
    // third -> value = 3;
    // third -> Next = NULL;

    // printList(head); 


    Node* head = TakeUserInput();
    
    printList(head);

    return 0; 
}