#include <iostream>
#include <deque>

using namespace std;

int main(){
    deque<string> book;
    bool f = true;
    string commands;
    string name_of_book;
    string erased_book;
    
    while(f){
        cin >> commands;
        if(commands == "add_front"){
            cin >> name_of_book;
            book.push_front(name_of_book);
            cout << "ok" << endl;
        }
        else if(commands == "add_back"){
            cin >> name_of_book;
            book.push_back(name_of_book);
            cout << "ok" << endl;
        }
        else if(commands == "erase_front"){
            if(book.empty()){
                cout << "error" << endl;
            }
            else{
                erased_book = book.front();
                book.pop_front();
                cout << erased_book << endl;
            }
        }
        else if(commands == "erase_back"){
            if(book.empty()){
                cout << "error" << endl;
            }
            else{
                erased_book = book.back();
                book.pop_back();
                cout << erased_book << endl;
            }
        }
        else if(commands == "front"){
            if(book.empty()){
                cout << "error" << endl;
            }
            else{
                cout << book.front() << endl;
            }
        }
        else if(commands == "back"){
            if(book.empty()){
                cout << "error" << endl;
            }
            else{
                cout << book.back() << endl;
            }
        }
        else if(commands == "clear"){
            book.clear();
            cout << "ok" << endl;
        }
        else if(commands == "exit"){
            cout << "goodbye" << endl;
            f = false;
        }





    }



}