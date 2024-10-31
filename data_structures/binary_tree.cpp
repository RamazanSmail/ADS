#include <iostream>
using namespace std;

struct Node{
    int data; //that stores a value
    Node* left; //left child
    Node* right; //right child
};

Node* createNode(int data){                                                                               
    Node* newNode = new Node();                                                                          
    newNode->data = data;                                                                               
    newNode->left = nullptr;  //because we dont have left and right childrens now                       
    newNode->right = nullptr;                                                                         
    return newNode;
}

int main(){
    //     1      We are creating such a binary tree
    //    / \
    //   2  3
    //  / 
    // 4

    Node* root = createNode(1);
    root->left = createNode(2);
    root->right = createNode(3);
    root->left->left = createNode(4);


    //Notice!!!: Binary tree can have only <=2 childrens, BST has same rule but also
    //should be like this form
    //       root
    //      /    \
    //  <=root   >root       right subtree should be always bigger, left subtree less or equal

    return 0;
}