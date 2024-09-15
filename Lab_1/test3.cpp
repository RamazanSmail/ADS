#include <iostream>
#include <vector>

using namespace std;

int main(){
    vector<int> myVector;
    myVector.push_back(2); //push_back добавляет двойку в конец вектора
    myVector.push_back(5);
    myVector.push_back(6);

    myVector[0] = 1000; //меняем значение числа под 0-вым индексом

    cout << myVector.at(1) << endl; //проверяет не вышли ли мы за границы нашего вектора

    myVector.pop_back(); //убирает последний элемент вектора


    for(int i = 0; i < myVector.size(); i++){  //size указывает количество элементов в векторе
        cout << myVector[i] << ' ';     // вытаскивает каждый элемент 
    }

    myVector.clear(); //очищает вектор

}