#include<iostream>

using namespace std;





int main(){
    int n;
    cin >> n;

    int near[n];

    int k;
    for(int i = 0; i < n; i++){
        cin >> near[i];
    }

    cin >> k;
    int differ;
    int max = 1000000000;
    int indexx;
    for(int i = 0; i < n; i++){
        int curr_dif = abs(near[i] - k);
        if(curr_dif < max){  //если абсолютная разница равна абсолютной разнице другого числа то пропускает этот цикл
            differ = curr_dif;
            max = differ;
            indexx = i;
        }

    }
    cout << indexx;
}
    