#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main() {
    int n;
    
    cin >> n;
    
    vector<int> numbers(n);
    
    for (int i = 0; i < n; i++) {
        cin >> numbers[i];
    }

    
    map<int, int> frequency;

    
    for (int num : numbers) {
        frequency[num]++;
    }

    
    int max_frequency = 0;
    for (auto pair : frequency) {
        if (pair.second > max_frequency) {
            max_frequency = pair.second;
        }
    }

   
    vector<int> modes;
    for (auto pair : frequency) {
        if (pair.second == max_frequency) {
            modes.push_back(pair.first);
        }
    }

    
    sort(modes.begin(), modes.end(), greater<int>());

    for (int mode : modes) {
        cout << mode << " ";
    }
    cout << endl;

    return 0;
}