#include <iostream> 
int main(){ int n; std::cin >> n; int a[n]; for(int i = 0; i < n; i++) std::cin >> a[i]; for(int i = 0; i < n; i = i + 2) std::cout << a[i] << " ";}