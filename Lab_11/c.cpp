#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> parents(20000);

int find_parent(int vertex){
    if(parents[vertex] == -1){
        return vertex;
    }
    return parents[vertex] = find_parent(parents[vertex]); // Path Compression
}

void union_sets(int a, int b){
    a = find_parent(a);
    b = find_parent(b);

    if(a < b) swap(a, b);

    if(a != b){
        parents[b] = a;
    }
}

int kruskals(vector<pair<int, pair<int, int>>>& edgeList){
    int totalWeight = 0;

    for(auto edge : edgeList){
        int weight = edge.first;
        int source = edge.second.first;
        int destination = edge.second.second;

        if(find_parent(source) != find_parent(destination)){
            totalWeight += weight;
            union_sets(source, destination);
        }
    }

    return totalWeight;
}

int main(){
    int n, m, bigCarCost, smallCarCost;
    cin >> n >> m >> bigCarCost >> smallCarCost;

    vector<pair<int, pair<int, int>>> edgeList; // weight, source, destination

    while(m--){
        string s;
        int source, destination, kilometersLong;

        cin >> s >> source >> destination >> kilometersLong;

        if(s == "both"){
            edgeList.push_back(make_pair(kilometersLong * bigCarCost, make_pair(source, destination)));
            edgeList.push_back(make_pair(kilometersLong * smallCarCost, make_pair(source, destination)));
        }
        else if(s == "big"){
            edgeList.push_back(make_pair(kilometersLong * bigCarCost, make_pair(source, destination)));
        }
        else{
            edgeList.push_back(make_pair(kilometersLong * smallCarCost, make_pair(source, destination)));
        }
    }

    sort(edgeList.begin(), edgeList.end());
    parents.resize(n);
    // r.resize(n, 0);
    for (int i = 0; i < n; ++i) {
        parents[i] = -1;
    }

    cout << kruskals(edgeList);
}