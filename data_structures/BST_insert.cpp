#include <iostream>
using namespace std;

struct Node{
    int data;
    Node* left;
    Node* right;
};

Node* createNode(int data){
    Node* newNode = new Node();
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

Node* insert(Node* node, int key){  //key is number we need to insert
    if(node == NULL){
        return createNode(key);
    }

    if(node->data == key){  //if key is already in the tree
        return node;
    }

    if(node->data < key){  //if key is bigger we need to put to the right subtree of root
        node->right = insert(node->right, key);
    }

    else{  //otherwise it needs to be in the lest subtree
        node->left = insert(node->left, key);
    }

    return node;
}
void inorder(Node* root){   //this function will print a sorted BST elements
    if(root != NULL){
        inorder(root->left);
        cout << root->data << " ";
        inorder(root->right);
    }
}
int main(){
// Creating the following BST
    //      50
    //     /  \
    //    30   70
    //   / \   / \
    //  20 40 60 80
    Node* root = createNode(50);
    root = insert(root, 30);
    root = insert(root, 20);
    root = insert(root, 40);
    root = insert(root, 70);
    root = insert(root, 60);
    root = insert(root, 80);
    root = insert(root, 25);

    inorder(root);
    return 0;
}