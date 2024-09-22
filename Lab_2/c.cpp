#include <iostream>
using namespace std;

struct Node{
    int value;
    Node* Next;
};

int main(){
    Node* head = NULL;
    Node* temp = NULL;
    int index=0;
    int n;
    cin>>n;
    for (int i = 0; i < n; ++i) {
        int value;
        cin >> value;
        Node* newNode = new Node();  
        newNode->value = value;
        newNode->Next = NULL; 
        if (head == NULL) {
           
            head = newNode;
        } else {
            
            temp->Next = newNode;
        }
        temp = newNode; 
    }
    Node* curr= head;
    while(curr!=NULL){
       if(index%2==0){
        cout<<curr->value<<" ";
       }
       curr=curr->Next;
       index++;
    }
    cout<<endl;

    return 0;
}

